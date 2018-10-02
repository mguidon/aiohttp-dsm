import sqlalchemy as sa

from contextlib import contextmanager

import simcore_dsm_sdk

def create_tables(url, engine=None):
    from simcore_service_dsm.models import users

    meta = sa.MetaData()
    if not engine:
        engine = sa.create_engine(url)

    meta.create_all(bind=engine, tables=[users])

@contextmanager
def api_client(cfg: simcore_dsm_sdk.Configuration) -> simcore_dsm_sdk.ApiClient:
    from simcore_dsm_sdk.rest import ApiException

    client = simcore_dsm_sdk.ApiClient(cfg)
    try:
        yield client
    except ApiException as err:
        print("%s\n" % err)
    finally:
        #NOTE: enforces to closing client session and connector.
        # this is a defect of the sdk
        del client.rest_client