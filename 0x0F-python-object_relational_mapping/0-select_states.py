#!/usr/bin/python3
import MySQLdb
from sys import argv as av
db = MySQLdb.connect(host='localhost', user=av[1], passwd=av[2], db=av[3], port=3306)
cur = db.cursor()
num_rows = cur.execute('SELECT * FROM states')
rows = cur.fetchall()
for row in rows:
    print (row)
