#/bin/bash
exec /home/guidon/devel/src/osparc-simcore/scripts/openapi/openapi_codegen.sh \
    -i ../data-storage-manager/src/simcore_service_dsm/oas3/v1/openapi.yaml \
    -o . \
    -g python \
    -c ./codegen_config.json
