#!/bin/bash

# TODO: PC i really do not like this. we should combine cookiecutter with parts in simcore-lib
#
# define the input specification file and the output directory
# typical structure:
# /src/package-name/.openapi/v1/package_api.yaml   -- this is the input file
# /src/package-name/rest/generated_code            -- this is the output directory

REPO_ROOT=/home/guidon/devel/src/osparc-simcore
SOURCE_DIR=../src/simcore_service_dsm
INPUT_SPEC=${SOURCE_DIR}/oas3/v1/openapi.yaml
OUTPUT_DIR=${SOURCE_DIR}/rest
OUTPUT_DIR_GEN=${SOURCE_DIR}/rest/generated_code
INIT_FILE_PATH=${OUTPUT_DIR}/__init__.py
HANDLERS_FILE_PATH=${OUTPUT_DIR}/handlers.py
ROUTING_FILE_PATH=${OUTPUT_DIR_GEN}/routing.py

# create the folder for the output
mkdir -p $OUTPUT_DIR
mkdir -p $OUTPUT_DIR_GEN

# generate the python server models code
ABSOLUTE_INPUT_PATH=$(realpath "${INPUT_SPEC}")
ABSOLUTE_OUTPUT_DIR=$(realpath "${OUTPUT_DIR}")
ABSOLUTE_OUTPUT_DIR_GEN=$(realpath "${OUTPUT_DIR_GEN}")
$REPO_ROOT/scripts/openapi/openapi_python_server_codegen.sh -i ${ABSOLUTE_INPUT_PATH} -o ${ABSOLUTE_OUTPUT_DIR_GEN}

# replace import entries in python code
find ${OUTPUT_DIR_GEN} -type f -exec sed -i 's/openapi_server.models././g' {} \;
find ${OUTPUT_DIR_GEN} -type f -exec sed -i 's/openapi_server/../g' {} \;

# create __init__.py if always
cat > "${INIT_FILE_PATH}" << EOF
"""GENERATED CODE from codegen.sh
It is advisable to not modify this code if possible.
This will be overriden next time the code generator is called.
"""
from .generated_code import (
    models,
    util,
    routing
)
EOF

# only generate stub if necessary
if [ ! -e "${HANDLERS_FILE_PATH}" ]; then
    cat > "${HANDLERS_FILE_PATH}" << EOF
"""This is a generated stub of handlers to be connected to the paths defined in the API

"""
import logging

from aiohttp import web_exceptions

log = logging.getLogger(__name__)

# This module shall contain the handlers of the API (implementation side of the openapi server side).
# Each operation is typically defined as
# async def root_get(request):
#   return "hello API world"

# The API shall define a path where the entry operationId:
# operationId: root_get
EOF
fi

# always generate routing
cat > "${ROUTING_FILE_PATH}" << EOF
"""GENERATED CODE from codegen.sh
It is advisable to not modify this code if possible.
This will be overriden next time the code generator is called.

use create_web_app to initialise the web application using the specification file.
The base folder is the root of the package.
"""


import logging
from pathlib import Path

from aiohttp import hdrs, web
from aiohttp_apiset import SwaggerRouter
from aiohttp_apiset.middlewares import Jsonify, jsonify
from aiohttp_apiset.swagger.loader import ExtendedSchemaFile
from aiohttp_apiset.swagger.operations import OperationIdMapping

from .. import handlers
from .models.base_model_ import Model
from .models.error import Error

log = logging.getLogger(__name__)

@web.middleware
async def __handle_errors(request, handler):
    try:
        response = await handler(request)
        return response
    except web.HTTPError as ex:
        error = Error(status=ex.status, message=ex.reason)
        error_dict = error.to_dict()
        return web.json_response(error_dict, status=ex.status)

def create_web_app(base_folder, spec_file, additional_middlewares = None):
    # create the default mapping of the operationId to the implementation code in handlers
    opmap = __create_default_operation_mapping(Path(base_folder / spec_file))

    # generate a version 3 of the API documentation
    router = SwaggerRouter(
        swagger_ui='/apidoc/',
        version_ui=3, # forces the use of version 3 by default
        search_dirs=[base_folder],
        default_validate=True,
    )

    # add automatic jsonification of the models located in generated code
    jsonify.singleton = Jsonify(indent=3, ensure_ascii=False)
    jsonify.singleton.add_converter(Model, lambda o: o.to_dict(), score=0)

    middlewares = [jsonify, __handle_errors]
    if additional_middlewares:
        middlewares.extend(additional_middlewares)
    # create the web application using the API
    app = web.Application(
        router=router,
        middlewares=middlewares,
    )
    router.set_cors(app, domains='*', headers=(
        (hdrs.ACCESS_CONTROL_EXPOSE_HEADERS, hdrs.AUTHORIZATION),
    ))

    # Include our specifications in a router,
    # is now available in the swagger-ui to the address http://localhost:8080/swagger/?spec=v1
    router.include(
        spec=Path(base_folder / spec_file),
        operationId_mapping=opmap,
        name='v1',  # name to access in swagger-ui,
        basePath="/v1" # BUG: in apiset with openapi 3.0.0 [Github bug entry](https://github.com/aamalev/aiohttp_apiset/issues/45)
    )

    return app

def __create_default_operation_mapping(specs_file):
    operation_mapping = {}
    yaml_specs = ExtendedSchemaFile(specs_file)
    paths = yaml_specs['paths']
    for path in paths.items():
        for method in path[1].items(): # can be get, post, patch, put, delete...
            op_str = "operationId"
            if op_str not in method[1]:
                raise Exception("The API %s does not contain the operationId tag for route %s %s" % (specs_file, path[0], method[0]))
            operation_id = method[1][op_str]
            operation_mapping[operation_id] = getattr(handlers, operation_id)
    return OperationIdMapping(**operation_mapping)
EOF
