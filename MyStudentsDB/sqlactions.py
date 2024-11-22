import sqlite3

connect = sqlite3.connect("./students.db")

cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students (
               
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        class TEXT
               
               );""")

def add_student_to_table(student, last_name, _class):
    cursor.execute(f"INSERT INTO students (name, last_name, class) VALUES (?, ?, ?);", (student, last_name, _class))
    connect.commit()

def _see_table(command):
    cursor.execute(command)
    rows = cursor.fetchall()
    for row in rows:
        print(" | ".join(str(k) for k in row))

def see_entire_table():
    _see_table("SELECT * FROM students;")

def search_by_name(name):
    _see_table(f"SELECT * FROM students WHERE LOWER(name) = LOWER('{name}');")