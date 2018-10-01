#/bin/bash
exec /home/guidon/devel/src/osparc-simcore/scripts/openapi/openapi_codegen.sh \
    -i ./swagger.json \
    -o . \
    -g python \
    -c ./codegen_config.json
