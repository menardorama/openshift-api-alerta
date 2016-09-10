#!/usr/bin/env python
import os

from datetime import datetime, timedelta
from pymongo import MongoClient

DB_NAME = os.environ['OPENSHIFT_APP_NAME']
DB_HOST = os.environ['OPENSHIFT_MONGODB_IP']
DB_PORT = int(os.environ['OPENSHIFT_MONGODB_PORT'])

client = MongoClient(DB_HOST, DB_PORT)
db = client[DB_NAME]

db.keys.insert_one({
    "user": "demo",
    "key": "demo-key",
    "text": "demo key",
    "expireTime": datetime.now() + timedelta(days=1000),
    "type": "read-write",
    "count": 0,
    "lastUsedTime": None
})
