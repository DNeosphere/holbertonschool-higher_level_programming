#!/usr/bin/python3
"""
Selects all states from a db
"""
import MySQLdb
from sys import argv

db = MySQLdb.connect(host="127.0.0.1", user=argv[1],
                     passwd=argv[2], db=argv[3])
cur = db.cursor()

cur.execute('SELECT * FROM states \
            WHERE name LIKE "N%" \
            ORDER BY states.id ASC;')
states = cur.fetchall()

for state in states:
    print(state)

cur.close()
db.close()
