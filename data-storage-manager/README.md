(export $(cat .env |grep = | xargs) && simcore-service-dsm --print-config)