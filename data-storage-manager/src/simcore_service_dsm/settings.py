""" Configuration file's schema

TODO: add more strict checks with re
"""
import argparse
import logging
import os

import trafaret_config as _tc
import trafaret_config.commandline as _tc_cli
import trafaret as T

from simcore_sdk.config import (
    db,
    s3
)

from . import resources

__version__ = "1.0"

log = logging.getLogger(__name__)

DEFAULT_CONFIG='config-test.yaml'
CONFIG_KEY="config"


_APP_SCHEMA = T.Dict({
    "host": T.IP,
    "port": T.Int(),
    "log_level": T.Enum("DEBUG", "WARNING", "INFO", "ERROR", "CRITICAL", "FATAL", "NOTSET"),
    "testing": T.Bool(),
    T.Key("disable_services", default=[], optional=True): T.List(T.String())
})

# TODO: add support for versioning.
#   - check shema fits version
#   - parse/format version in schema
CONFIG_SCHEMA_V1 = T.Dict({
    "version": T.String(),
    T.Key("app"): _APP_SCHEMA,
    T.Key("postgres"): db.CONFIG_SCHEMA,
    T.Key("s3"): s3.CONFIG_SCHEMA
})

CONFIG_SCHEMA = CONFIG_SCHEMA_V1



def dict_from_class(cls) -> dict:
    return dict( (key, getattr(cls, key)) for key in dir(cls)  if not key.startswith("_")  )


def add_cli_options(argument_parser=None):
    """
        Adds settings group to cli with options:

        -c CONFIG, --config CONFIG
                                Configuration file (default: 'config.yaml')
        --print-config        Print config as it is read after parsing and exit
        --print-config-vars   Print variables used in configuration file
        -C, --check-config    Check configuration and exit
    """
    if argument_parser is None:
        argument_parser = argparse.ArgumentParser()

    _tc.commandline.standard_argparse_options(
        argument_parser.add_argument_group('settings'),
        default_config=DEFAULT_CONFIG)

    return argument_parser


def config_from_options(options, vars=None): # pylint: disable=W0622
    if vars is None:
        vars = os.environ

    if not os.path.exists(options.config):
        resource_name = options.config
        if resources.exists(resource_name):
            options.config = resources.get_path(resource_name)
        else:
            resource_name = resources.RESOURCE_CONFIG + '/' + resource_name
            if resources.exists(resource_name):
                options.config = resources.get_path(resource_name)

    log.debug("loading %s", options.config)

    return _tc_cli.config_from_options(options, trafaret=CONFIG_SCHEMA, vars=vars)

def read_and_validate(filepath, vars=None): # pylint: disable=W0622
    if vars is None:
        vars = os.environ
    # NOTE: vars=os.environ in signature freezes default to os.environ before it gets
    # Cannot user functools.partial because os.environ gets then frozen
    return _tc.read_and_validate(filepath, trafaret=CONFIG_SCHEMA, vars=vars)


def config_from_file(filepath) -> dict:
    """
        Loads and validates app configuration from file
        Some values in the configuration are defined as environment variables

        Raises trafaret_config.ConfigError
    """
    config = _tc.read_and_validate(filepath, CONFIG_SCHEMA, vars=os.environ)
    return config

__all__ = (
    'CONFIG_SCHEMA',
    'add_cli_options',
    'config_from_options',
    'config_from_file',
    'read_and_validate'
)
