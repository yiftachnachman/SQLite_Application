import sqlite3
from Student import Student

conn = sqlite3.connect('StudentDB')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS Student(StudentId INTEGER PRIMARY KEY AUTOINCREMENT,FirstName VARCHAR(25) NOT NULL,LastName VARCHAR(25) NOT NULL,GPA NUMERIC NOT NULL ,Major VARCHAR(10) NOT NULL,FacultyAdvisor VARCHAR(25) NOT NULL)")

print ("1: Display All Students and all their attributes ")
print ("2: Create Students")
print ("3: Update Students")
print ("4: Delete Students by StudentId")
print ("5: Search and Display students by Major, GPA and Advisor.")

userAnswer = int(input("Enter in your choice \n# "))

if (userAnswer == 1):
    c.execute("SELECT * From Student")
    row = c.fetchall()
    for row in row:
        print(row)

if (userAnswer == 2):
    first_name = input("Enter in the first name")
    last_name = input("Enter in the last name")
    gpa = float(input("Enter in the GPA"))
    major = input("Enter in the major")
    faculty_advisor = input("Enter in the faculty advisor")
    c.execute("INSERT INTO Student (FirstName, LastName, GPA, Major, FacultyAdvisor) values (?,?,?,?,?), (first_name, last_name, gpa, major, faculty_advisor)")

if(userAnswer == 3):
    answer = int(input("would you like to update your faculty advisor (1) or major(2)"))
    if answer == 1:
        c.execute("SELECT * FROM Student WHERE StudentID")
        students = c.fetchall()
        for students in students:
            print(students)
        conn.commit()
        ID = int(input("Please enter the ID of the student whose Faculty Advisor would you like to update?\n"))
        faculty = input("Please enter the name of the Faculty Advisor you would like to change to \n")
        c.execute(''' UPDATE Student set FacultyAdvisor=? WHERE StudentID=?''', (faculty, ID))
        conn.commit()
        print("Your Faculty Advisor has been updated for that student")
    elif answer == 2:
        c.execute("SELECT * FROM Student WHERE StudentID")
        students = c.fetchall()
        for students in students:
            print(students)
        conn.commit()
        ID = int(input("Please enter the ID of the student whose major would you like to update?\n"))
        major = input("Please enter the name of the major you would like to change to \n")
        c.execute(''' UPDATE Student set Major=? WHERE StudentID=?''', (major, ID))
        conn.commit()
        print("Your Major has been updated for that student")
    else:
        print("Invalid entry. Please try again")

if(userAnswer == 4):
    c.execute("SELECT * FROM Student WHERE StudentID")
    students = c.fetchall()
    for students in students:
        print(students)
    conn.commit()
    answer = input("Please enter in student ID who you want to take out?\n")
    c.execute("DELETE FROM Student WHERE StudentID=?", (answer,))
    conn.commit()
    print("Student has been deleted from your database")

if (userAnswer == 5):
    c.execute("SELECT * FROM Student")
    students = c.fetchall()
    for students in students:
        print(students)
    conn.commit()
    answer = int(input("Would you like to search by Major(1), GPA(2), or Faculty Advisor(3)?\n"))
    if (answer == 1):
        major = input("What is the major that you would like to search for?\n")
        c.execute(''' SELECT * FROM Student WHERE Major=?''', (major,))
        for row in c.fetchall():
            print(row)
    elif (answer == 2):
        gpa = input("What is the GPA that you would like to search for?\n")
        c.execute(''' SELECT * FROM Student WHERE GPA=?''', (gpa,))
        for row in c.fetchall():
            print(row)
    else:
        facultyadvisor = input("Who is the Faculty Advisor that you would like to search for?\n")
        c.execute(''' SELECT * FROM Student WHERE FacultyAdvisor=?''', (facultyadvisor,))
        for row in c.fetchall():
            print(row)