#!/usr/bin/python3
"""Select a table in a database"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
         host="localhost",
         user=sys.argv[1],
         passwd=sys.argv[2],
         db=sys.argv[3],
         port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM {} ORDER BY {}".format('states', 'id'))

    for row in cur.fetchall():
        if row[1] == sys.argv[4]:
            print(row)

    db.close()
