"""
    PROGRAM :  Hall of Prophecy
    AUTHOR  :  Laura Purcell-Gates
    EMAIL   :  <laurapurcellgates@gmail.com>

    CS50x 2023 Practice Problem 7 Hall of Prophecy

    I refactored a SQL database to avoid redundancies, and 
    wrote a Python program to load new SQL tables linking 
    students to house assignments. 

    My refactored database and schema are roster.db and schema.sql.
    Original database and schema roster-orig.db and schema-orig.sql.

    Code fully written by me; no pre-filled CS50 code.

    Link to the practice problem:
    https://cs50.harvard.edu/x/2023/problems/7/prophecy/  """

import csv
from cs50 import SQL

# access roster db
db = SQL("sqlite:///roster.db")

# open csv file, copy info to tables in roster.db
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for record in reader:
        # grab student, house and head names
        student = record['student_name']
        house = record['house']
        head = record['head']

        # insert student names to students table, ignoring UNIQUE clashes
        db.execute("INSERT OR IGNORE INTO students(student_name) VALUES(?);", student)

        # insert house names to houses table, ignoring UNIQUE clashes
        db.execute("INSERT OR IGNORE INTO houses(house_name, head) VALUES(?, ?);", house, head)

        # LINK STUDENT ID TO HOUSE ID IN ASSIGNMENTS TABLE
        # extract student id from students table
        rows = db.execute("SELECT * FROM students WHERE student_name = ?;", student)

        # insert student and house ids into assignments table
        for row in rows:
            student_id = row['id']
            house_ids = db.execute("SELECT id FROM houses WHERE house_name = ?;", house)
            for house_id in house_ids:
                db.execute("INSERT OR IGNORE INTO assignments(student_id, house_id) VALUES(?, ?);", student_id, house_id['id'])







