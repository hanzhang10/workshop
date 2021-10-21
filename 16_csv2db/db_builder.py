# Team Whales: Hebe Huang, Josephine Lee, Han Zhang
# SoftDev
# K16: All About Database
# 2021-10-21

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect("Whales") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
c.execute("CREATE TABLE roster(name TEXT, age INTEGER, id INTEGER)")

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
with open("students.csv", mode = 'r') as students:  #reads in csv file
    file = csv.DictReader(students)
    for lines in file:                              #iterates through csv rows
        name = file['name']
        age = file['age']
        id = file['id']
        script = "INSERT INTO roster VALUES(\"" + name + "\"," + age + "," + id + ")" #scripts 
        c.execute(script)

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database

#open db if exists, otherwise create
db = sqlite3.connect("foo")

c = db.cursor() #facilitate db ops

c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")

db.commit() #save changes
db.close()
