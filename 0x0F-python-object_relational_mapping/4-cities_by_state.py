#!/usr/bin/python3
"""Select a table in a database"""


import MySQLdb
import sys


def check_command(string=''):
    if ';' in string:
        return False
    else:
        return True


if __name__ == "__main__":
    db = MySQLdb.connect(
         host="localhost",
         user=sys.argv[1],
         passwd=sys.argv[2],
         db=sys.argv[3],
         port=3306)

    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM states RIGHT JOIN cities on
                states.id = cities.state_id""")

    for row in cur.fetchall():
        print(row)

    db.close()
