import collections
import logging
import os
import pathlib
import sys
import uuid
from random import randrange

import pytest
import requests
import sqlalchemy as sa
import utils
import simcore_service_dsm
from s3wrapper.s3_client import S3Client

from simcore_service_dsm.models import FileMetaData

pytest_plugins = ("aiohttp",)

CURRENT_DIR = pathlib.Path(sys.argv[0] if __name__ == "__main__" else __file__).parent.absolute()
log = logging.getLogger(__name__)

@pytest.fixture(scope='session')
def package_paths(pytestconfig):
    # Intentionally not using resource paths so we have an alternative
    # way to retrieve paths to test resource logic itself
    package_root = CURRENT_DIR.parent
    src_folder = package_root / "src"
    test_folder = package_root / "tests"

    paths={}
    paths["ROOT_FOLDER"] = package_root
    paths["SRC_FOLDER"] = src_folder
    paths["PACKAGE_FOLDER"] = src_folder / simcore_service_dsm.__name__
    paths["TEST_FOLDER"] = test_folder

    for key, path in paths.items():
        assert path.exists(), "Invalid path in %s" % key

    return collections.namedtuple("PackagePaths", paths.keys())(**paths)


DATABASE = 'aio_login_tests'
USER = 'admin'
PASS = 'admin'

def is_postgres_responsive(url):
    """Check if something responds to ``url``."""
    try:
        engine = sa.create_engine(url)
        conn = engine.connect()
        conn.close()
    except sa.exc.OperationalError:
        return False
    return True

def is_responsive(url, code=200):
    """Check if something responds to ``url``."""
    try:
        response = requests.get(url)
        if response.status_code == code:
            return True
    except requests.exceptions.RequestException as _e:
        pass
    
    return False

@pytest.fixture(scope='session')
def docker_compose_file():
    """
      Path to docker-compose configuration files used for testing
      - fixture defined in pytest-docker
    """
    old = os.environ.copy()
    
    os.environ['POSTGRES_DB']=DATABASE
    os.environ['POSTGRES_USER']=USER
    os.environ['POSTGRES_PASSWORD']=PASS
    os.environ['POSTGRES_ENDPOINT']="FOO"

    dc_path = CURRENT_DIR / 'docker-compose.yml'

    assert dc_path.exists()
    yield str(dc_path)

    os.environ = old

@pytest.fixture(scope='session')
def postgres_service(docker_services, docker_ip):
    url = 'postgresql://{user}:{password}@{host}:{port}/{database}'.format(
        user = USER,
        password = PASS,
        database = DATABASE,
        host=docker_ip,
        port=docker_services.port_for('postgres', 5432),
    )

    # Wait until service is responsive.
    docker_services.wait_until_responsive(
        check=lambda: is_postgres_responsive(url),
        timeout=30.0,
        pause=0.1,
    )

    return url


def create_app():
    from simcore_service_dsm.__main__ import parse
    from simcore_service_dsm import app
    cmd = "-c {}".format(CURRENT_DIR/"data/config-db.yaml").split()
    config = parse(cmd)
    return app.create(config)

@pytest.fixture()
def test_client(postgres_service, loop, aiohttp_client):
    _app = create_app()
    cli = loop.run_until_complete(aiohttp_client(_app))
    print(cli.host, cli.port)
    return cli


@pytest.fixture()
def test_server(postgres_service, loop, aiohttp_server):
    _app = create_app()
    server = loop.run_until_complete(aiohttp_server(_app))
    print(server.host, server.port)
    return server

@pytest.fixture(scope="module")
def s3_client(docker_ip, docker_services):
    """wait for minio to be up"""

    # Build URL to service listening on random port.
    url = 'http://%s:%d/' % (
        docker_ip,
        docker_services.port_for('minio', 9000),
    )

    # Wait until service is responsive.
    docker_services.wait_until_responsive(
        check=lambda: is_responsive(url, 403),
        timeout=30.0,
        pause=0.1,
    )

    endpoint = '{ip}:{port}'.format(ip=docker_ip, port=docker_services.port_for('minio', 9000))
    access_key = "12345678"
    secret_key = "12345678"
    secure = False
    s3_client = S3Client(endpoint, access_key, secret_key, secure)
    return s3_client

@pytest.fixture(scope="function")
def tmp_files(tmpdir_factory):
    def _create_files(N):
        filepaths = []
        for _i in range(N):
            name = str(uuid.uuid4())
            filepath = os.path.normpath(str(tmpdir_factory.mktemp('data').join(name + ".txt")))
            with open(filepath, 'w') as fout:
                fout.write("Hello world\n")
            filepaths.append(filepath)

        return filepaths
    return _create_files


@pytest.fixture(scope="function")
def dsm_mockup_db(postgres_service, s3_client, tmp_files):
    utils.create_tables(url=postgres_service)
    bucket_name = utils.bucket_name()
    s3_client.create_bucket(bucket_name, delete_contents_if_exists=True)

    users = [ 'alice', 'bob', 'chuck', 'dennis']

    projects = ['astronomy', 'biology', 'chemistry', 'dermatology', 'economics', 'futurology', 'geology']
    location = "simcore.s3"

    nodes = ['alpha', 'beta', 'gamma', 'delta']

    N = 100

    files = tmp_files(N)
    counter = 0
    data = {}
    for _file in files:
        idx = randrange(len(users))
        user = users[idx]
        user_id = idx + 10
        idx =  randrange(len(projects))
        project = projects[idx]
        project_id = idx + 100
        idx =  randrange(len(nodes))
        node = nodes[idx]
        node_id = idx + 10000
        file_id = str(uuid.uuid4())
        file_name = str(counter)
        counter = counter + 1
        object_name = os.path.join(str(project_id), str(node_id), str(counter))
        assert s3_client.upload_file(bucket_name, object_name, _file)


        d = { 'object_name' : object_name,
              'bucket_name' : bucket_name, 
              'file_id' : file_id,
              'file_name' : file_name,
              'user_id' : user_id,
              'user_name' : user,
              'location' : location,
              'project_id' : project_id,
              'project_name' : project,
              'node_id' : node_id,
              'node_name' : node
             }

        data[object_name] = FileMetaData(**d)


        utils.insert_metadata(postgres_service, object_name, bucket_name, file_id, file_name, user_id,
            user, location, project_id, project, node_id, node)

   
    total_count = 0
    for _obj in s3_client.list_objects_v2(bucket_name, recursive = True):
        total_count = total_count + 1

    assert total_count == N
    yield data

    s3_client.remove_bucket(bucket_name, delete_contents=True)
    utils.drop_tables(url=postgres_service)
