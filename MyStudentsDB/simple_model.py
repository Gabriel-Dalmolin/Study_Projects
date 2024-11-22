from sqlactions import *

while True:
    print()
    print("-"*50)
    print("What do you want to do?")
    print("1 - Add student")
    print("2 - See students")
    print("3 - Search student by name")
    print("-"*50)
    action = input()
    if action == "1":
        student_name = input("What is the student name?\n")
        student_last_name = input("What is the student last name?\n")
        student_class = input("What is the student class?\n")
        if student_class and student_name:
            add_student_to_table(student_name, student_last_name, student_class)
        else:
            print("Error, not recognized class or name of the student")
    elif action == "2":
        see_entire_table()
    elif action == "3":
        name = input("What is the student's name?\n")
        search_by_name(name)
    else:
        print("action not recognized")
