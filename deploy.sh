#!/bin/sh

rhc app create api python-2.7 mongodb-2.4 \
AUTH_REQUIRED=True \
CLIENT_ID=$CLIENT_ID \
CLIENT_SECRET=$CLIENT_SECRET \
--from-code=git://github.com/alerta/openshift-api-alerta.git

rhc alias add -a api api.alerta.io