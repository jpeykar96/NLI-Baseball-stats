#!/usr/bin/python
import MySQLdb
import sys

a = ""
for item in sys.argv:
    if item != "main.py":
        a += item + " "
a.strip(' ')
# print a

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="123",  # your password
                     db="stats")        # name of the data base

cur = db.cursor()

mapping = ["hit","threw","won","coached","studied","played"]
input = a.split(" ")
action = ""
for word in mapping:
    if word in input:
        action = word

if action is "hit":
    objectDone = ""
    moreLess = ""
    numberR = 0
    for s in input:
        if s.isdigit():
            numberR = s
    numberT = int(numberR)
    numberB = str(numberT)
    if "single" in input:
        objectDone = 'H'
    elif "double" in input:
        objectDone = "2B"
    elif "triple" in input:
        objectDone = "3B"
    elif "homerun" in input:
        objectDone = "HR"
    elif "rbi" in input:
        objectDone = "RBI"
    elif "walk" in input:
        objectDone = "BB"

    if "more" in input:
        moreLess = ">"
    elif "less" in input:
        moreLess = "<"
    else:
        moreLess = "="
    selectCl = "SELECT M.nameFirst, M.nameLast,"
    selectCl  = selectCl + "B."+objectDone + " "
    fromCl = "FROM batting as B, master as M "
    whereCl = "WHERE B.playerID = M.playerID AND B." + objectDone + moreLess + numberB
    finalQuery = selectCl + fromCl + whereCl
    print finalQuery
    cur.execute(finalQuery)
# Use all the SQL you like
# cur.execute("SELECT playerID, hr FROM batting as b WHERE b.hr>50")

for row in cur.fetchall():
    retRow = ""
    for col in row:
        retRow += str(col) + " "
    retRow.strip(" ")
    print retRow

db.close()
