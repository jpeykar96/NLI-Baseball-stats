#!/usr/bin/python
import MySQLdb
import sys

a = ""
for item in sys.argv:
    if item != "main.py":
        a += item + " "
a.strip(' ')
print a

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="123",  # your password
                     db="stats")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM teams")

# for row in cur.fetchall():
    # print row[0]

db.close()
