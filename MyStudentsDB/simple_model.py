from sqlactions import *

while True:
    print()
    print("-"*50)
    print("What do you want to do?")
    print("1 - Add student")
    print("2 - Access student grade")
    print("3 - Search student by name")
    print("4 - Remove student from the table")
    print("-"*50)
    action = input()

    if action == "1":
        student_name = input("What is the student name?\n").strip()
        student_last_name = input("What is the student last name?\n").strip()
        student_class = input("What is the student class?\n").strip()
        if student_class and student_name:
            add_student_to_table(student_name, student_last_name, student_class)
        else:
            print("Error, not recognized class or name of the student")

    elif action == "2":
        see_entire_table()
        print()
        print("-"*50)
        print("Print the ID of the selected student, or, print Q to go back")
        print("-"*50)
        student_id = input()
        if student_id.lower() == "q":
            pass
        else:
            student_id = int(student_id)
            access_student_table(student_id)
            print("-"*50)
            print("What do you want to do?")
            print("1 - Add grades")
            print("Q - Quit")
            print("-"*50)
            action = input()
            if action == "1":
                test_code = input("What is the identifier code of the test? ")
                year = input("What is the year of it? ")
                semester = input("What is the semester? ")
                grade = input("What is the grade? ")
                add_into_student_table(student_id, test_code, year, semester, grade)
            elif action.lower() == "Q":
                pass

    elif action == "3":
        name = input("What is the student's name?\n")
        search_by_name(name)

    elif action == "4":
        see_entire_table()
        student = input("What is the id of the student that you want to delete?\n").strip()
        delete_student(student)

    else:
        print("action not recognized")
