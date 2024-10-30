#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
 and lists all cities of that state, using the database hbtn_0e_4_usa
 """

from sys import argv
import MySQLdb

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])

    cur = conn.cursor()
    query = """ SELECT cities.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE BINARY states.name = %s
                ORDER BY cities.id ASC;
            """
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    first = True
    for row in rows:
        if not first:
            print(", ", end="")
        print(row[0], end="")
        first = False
    print()
    cur.close()
    conn.close()
