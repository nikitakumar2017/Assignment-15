#Q.1- Write a python script to create a database of students named Students.
import sqlite3
try:
    con=sqlite3.connect('student.db')
    print(con)
finally:
    con.close()
    print('DONE!!')

#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
student_info=[]
for i in range(1,11):
    student=[]
    print("Information of student no.",i)
    name=input("Name")
    marks=int(input("Marks"))
    student.append(name)
    student.append(marks)
    student=tuple(student)
    student_info.append(student) 
#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
    ''' Creating Table '''
import sqlite3
try:
    con=sqlite3.connect('student.db')
    cursor=con.cursor()
    query='create table student(name varchar(20),marks number(3) check (marks>=0 and marks<=100))'
    cursor.execute(query)
    print('Table Created Succesfully')
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem Occured')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done')

''' Inserting Values '''
import sqlite3
try:
    con=sqlite3.connect('student.db')
    cursor=con.cursor()
    query='insert into student values (?,?)'
    cursor.executemany(query,student_info)
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem Occured')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done')

#Q.4- Print the names of all the students who scored more than 80 marks.
import sqlite3
try:
    con=sqlite3.connect('student.db')
    cursor=con.cursor()
    query='Select * from student where marks>80'
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print('Name: {}, Marks: {}'.format(row[0],row[1]))
    con.commit()
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem Occured')
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done')
    
