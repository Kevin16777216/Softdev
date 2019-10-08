#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"
COURSE_FILE = "courses.csv";
STUDENT_FILE = "students.csv";

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
with open(STUDENT_FILE, newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     test = "CREATE TABLE students (code TEXT,mark INTEGER, id INTEGER PRIMARY KEY);"
     c.execute(test)
     for row in reader:
         test = "INSERT INTO students VALUES "+row['id']
         print(test)

c.execute("SELECT * FROM students;")
with open(COURSE_FILE, newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      headers = next(reader)
      print(headers)
      for row in reader:
        print(row)
c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database#Clyde "Thluffy" Sinclair
