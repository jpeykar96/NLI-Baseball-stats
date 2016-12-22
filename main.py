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

mapping = ["hit","threw","team"]
input = a.split(" ")
action = ""
for word in mapping:
    if word in input:
        action = word

if "more" in input:
    moreLess = ">"
elif "less" in input:
    moreLess = "<"
else:
    moreLess = "="

numberR = 0
for s in input:
    if s.isdigit():
        numberR = s
numberT = int(numberR)
numberB = str(numberT)

if action is "hit":
    objectDone = ""

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
    elif "bat" in input:
        objectDone = "AB"
    elif "stole" in input:
        objectDone = "SB"


    selectCl = "SELECT M.nameFirst, M.nameLast, B.yearID,"
    selectCl  = selectCl + "B."+objectDone + " "
    fromCl = "FROM batting as B, master as M "
    whereCl = "WHERE B.playerID = M.playerID AND B." + objectDone + moreLess + numberB
    finalQuery = selectCl + fromCl + whereCl
    cur.execute(finalQuery)

elif action is "threw":
    objectDone = ""
    if "won" in input:
        objectDone = 'W'
    elif "win" in input:
        objectDone = "W"
    elif "lost" in input:
        objectDone = "L"
    elif "complete" in input:
        objectDone = "CG"
    elif "shutout" in input:
        objectDone = "SHO"
    elif "strikeout" in input:
        objectDone = "SO"
    elif "homerun" in input:
        objectDone = "HR"
    elif "save" in input:
        objectDone = "SV"

    selectCl = "SELECT M.nameFirst, M.nameLast, P.yearID,"
    selectCl  = selectCl + "P."+objectDone + " "
    fromCl = "FROM pitching as P, master as M "
    whereCl = "WHERE P.playerID = M.playerID AND P." + objectDone + moreLess + numberB
    finalQuery = selectCl + fromCl + whereCl
    cur.execute(finalQuery)

elif action is "team":
    objectDone = ""
    if "won" in input:
        objectDone = 'W'
    elif "win" in input:
        objectDone = "W"
    elif "lost" in input:
        objectDone = "L"
    elif "complete" in input:
        objectDone = "CG"
    elif "shutout" in input:
        objectDone = "SHO"
    elif "strikeout" in input:
        objectDone = "SO"
    elif "homerun" in input:
        objectDone = "HR"
    elif "save" in input:
        objectDone = "SV"

    selectCl = "SELECT M.nameFirst, M.nameLast, P.yearID,"
    selectCl  = selectCl + "P."+objectDone + " "
    fromCl = "FROM pitching as P, master as M "
    whereCl = "WHERE P.playerID = M.playerID AND P." + objectDone + moreLess + numberB
    finalQuery = selectCl + fromCl + whereCl
    cur.execute(finalQuery)

for row in cur.fetchall():
    retRow = ""
    for col in row:
        retRow += str(col) + " "
    retRow.strip(" ")
    print retRow

db.close()
