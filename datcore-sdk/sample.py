# install package like so:
# pip install -v  pip install -v  git+https://github.com/ITISFoundation/osparc-simcore.git@webserver-sdk#subdirectory=packages/webserver-sdk/python
#
from contextlib import contextmanager
import asyncio
import simcore_dsm_sdk
import json
import re


from simcore_dsm_sdk.rest import ApiException
from simcore_dsm_sdk.models import HealthInfo


@contextmanager
def api_client(cfg):
    client = simcore_dsm_sdk.ApiClient(cfg)
    try:
        yield client
    except ApiException as err:
        print("%s\n" % err)
    finally:
        #NOTE: enforces to closing client session and connector.
        # this is a defect of the sdk
        del client.rest_client


async def run_test():
    cfg = simcore_dsm_sdk.Configuration()
    cfg.host = cfg.host.format(
        host="localhost",
        port=8080,
        version="v1"
    )

    with api_client(cfg) as client:
        api = simcore_dsm_sdk.DefaultApi(client)
        res = await api.health_check()

        assert isinstance(res, HealthInfo)
        assert res.last_access == -1
        
        last_access = 0
        for _ in range(5):
            check = await api.health_check()
            print(check.last_access)
            assert last_access < check.last_access
            last_access = check.last_access

       
loop = asyncio.get_event_loop()
loop.run_until_complete(run_test())
