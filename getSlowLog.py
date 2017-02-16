#!/usr/bin/env python
#
import sys

try:
    import pymongo
except ImportError as e:
    print(e)
    sys.exit()

import bson
import config
import datetime
from jinja2 import Template
from templates.mongodb_slowlog import html_str

def _conn(host, port, user=None, password=None, auth_db="admin"):
    from pymongo.errors import PyMongoError
    conn = pymongo.MongoClient(host, port)

    if user and password:
        db = conn[auth_db]
        try:
            db.authenticate(user, password=password)
        except PyMongoError:
            sys.exit("Username/Password incorrect")

    return conn

def convertTime(Time):
    tm = bson.Timestamp(Time, 1)
    return tm.as_datetime()

def getProfile(startTime, stopTime):
    exclude_dbs = ['local', 'test']
    for dbinfo in config.dbs:
        conn = _conn(dbinfo['host'],dbinfo['port'],dbinfo['user'],dbinfo['password'],dbinfo['auth_db'])
        for database in [d for d in conn.database_names() if d not in exclude_dbs]:
            db_conn = getattr(conn, database)
            if db_conn.profiling_level():
                sql = {'ts':{"$lt":startTime, "$gt":stopTime}, "op":{"$nin":['getmore','command']}}
                # db.setProfilingLevel(1,10);
                dbinfo['slow_log'].append(list(db_conn.system.profile.find(sql)))

                template = Template(html_str)
                rest_html = template.render(db_info = dbinfo)
                f = open('static/mongodb_slowlog.html', 'w')
                f.write(rest_html)
                f.close()

if __name__ == '__main__':
    startTime = convertTime(datetime.datetime.today())
    stopTime = convertTime(startTime + datetime.timedelta(days=-1))
    getProfile(startTime,stopTime)

