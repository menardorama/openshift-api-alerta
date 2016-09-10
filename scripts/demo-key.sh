#!/bin/sh

mongo -u ${OPENSHIFT_MONGODB_DB_USERNAME} -p ${OPENSHIFT_MONGODB_DB_PASSWORD} \
${OPENSHIFT_MONGODB_DB_HOST}:${OPENSHIFT_MONGODB_DB_PORT}/${OPENSHIFT_APP_NAME} \
--eval '
db.keys.insert({
    "user": "demo",
    "key": "demo-key",
    "text": "demo key",
    "expireTime": ISODate("2016-06-20T13:41:39.869Z"),
    "type": "read-write",
    "count": 0,
    "lastUsedTime": null
})'