#!/usr/bin/python3
""" Import modules: MySQLdb to interacat with our db
sys.argv to use cli args"""

import MySQLdb
from sys import argv as av
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=av[1],
                         passwd=av[2],
                         db=av[3],
                         port=3306)
    cur = db.cursor()
    num_rows = cur.execute('SELECT * FROM states WHERE name LIKE UPPER "N%"')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
