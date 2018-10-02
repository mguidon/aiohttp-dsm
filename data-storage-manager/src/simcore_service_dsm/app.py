""" Main application

"""
import logging

from aiohttp import web

from .db import setup_db
from .rest import setup_rest, create_router
from .session import setup_session
from .settings import CONFIG_KEY

log = logging.getLogger(__name__)

def create(config):
    """
        Initializes service
    """
    log.debug("Initializing app ... ")

    app = web.Application(router=create_router())
    app[CONFIG_KEY] = config
    

    setup_db(app)
    setup_session(app)
    setup_rest(app)

    return app

def run(config):
    """ Runs service

    NOTICE it is sync!
    """
    log.debug("Serving app ... ")

    app = create(config)
    web.run_app(app,
                host=config["app"]["host"],
                port=config["app"]["port"])

