""" Main application

"""
import logging

from aiohttp import web

from .db import setup_db
from .rest import setup_rest, create_router
from .session import setup_session


log = logging.getLogger(__name__)

def init_app(config):
    """
        Initializes service
    """
    log.debug("Initializing app ... ")

    app = web.Application(router=create_router())
    app["config"] = config
    

    setup_db(app)
    setup_session(app)
    setup_rest(app)

    return app

def run(config):
    """ Runs service

    NOTICE it is sync!
    """
    log.debug("Serving app ... ")

    app = init_app(config)
    web.run_app(app,
                host=config["app"]["host"],
                port=config["app"]["port"])
