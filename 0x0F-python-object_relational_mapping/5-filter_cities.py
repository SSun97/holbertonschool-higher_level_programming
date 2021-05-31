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
    print("SELECT cities.name FROM cities, states\
                WHERE cities.state_id = states.id\
                AND states.name='{}'".format(sys.argv[4]))
    cur.execute("SELECT cities.name FROM cities, states\
                WHERE cities.state_id = states.id\
                AND states.name='{}'".format(sys.argv[4]))

    list = []
    for row in cur.fetchall():
        list.append(row[0])

    if list == []:
        print()
    else:
        print(list, sep=", ")

    db.close()
