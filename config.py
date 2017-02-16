import MySQLdb

DBINFO = {'host': '10.0.0.1',
          'port': 3306,
          'user': 'noc',
          'password': '123.com',
          'db': 'ops_noc',
          'table': 'ops_resource'
          #grant select,insert,delete,update,create on ops_noc.* to 'noc'@'10.%' identified by '123.com';
          }

def mysql(sql):
    try:
        conn = MySQLdb.connect(host=DBINFO['host'],
                               user=DBINFO['user'],
                               passwd=DBINFO['password'],
                               port=DBINFO['port'],
                               db=DBINFO['db'],
                               connect_timeout=10
                               )
        conn.set_character_set('utf8')
        cur = conn.cursor()
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')
        cur.execute(sql)
        conn.commit()
        conn.close()
    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        exit(2)

dbs = [{'host': '10.0.0.1', 'port': 9501, 'user': None, 'password': None, 'auth_db': 'admin', 'slow_log': list(),'abbreviated': list()},

       ]
