from aiohttp import web

from .session import get_session
import time

__version__ = "0.0.0"

async def health_check(request):
    session = await get_session(request)

    data = {
        'name':__name__.split('.')[0], 
        'version': __version__,
        'status': 'RUNNING_FINE',
        'last_access' : session.get("last", -1.)
    }
#    import pdb; pdb.set_trace()
    session["last"] = time.time()
    return web.json_response(data, status=200)