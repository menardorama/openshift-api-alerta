#!/bin/bash

date >>${OPENSHIFT_PYTHON_LOG_DIR}/cron.log

coilmq -b ${OPENSHIFT_PYTHON_IP} -p 15000 -d >>${OPENSHIFT_PYTHON_LOG_DIR}/cron.log
alerta --pid-dir ${OPENSHIFT_TMP_DIR} >>${OPENSHIFT_PYTHON_LOG_DIR}/cron.log

