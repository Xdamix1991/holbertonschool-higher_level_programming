#!/usr/bin/python3
"""
this moduloe contains a script to list all states from hbtn_0e_0_usa
"""

import MySQLdb


conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="",
                       db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
