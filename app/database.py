import sqlite3
from contextlib import contextmanager  ##helps and handles the connection to the database

sqlite_file_name = "school.db"

@contextmanager
def get_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection   ##is like return
        connection.commit()
    finally:
        connection.close()

def create_table(): ##create table
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           country TEXT NOT NULL,
                           id_number INTEGER NOT NULL )''')

        connection.execute('''CREATE TABLE IF NOT EXISTS teachers(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           course_teaching TEXT NOT NULL,
                           experience TEXT NOT NULL,
                           education_level TEXT NOT NULL )''')
        
  
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                           course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name_of_course TEXT NOT NULL,
                           subtopics INTEGER NOT NULL,
                           duration_of_course INTEGER NOT NULL,
                           field_of_course TEXT NOT NULL )''')
        
        
def add_student(id,name,age,email,country, id_number): ##insert data
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students(id,name,age,email,country,id_number) VALUES (?,?,?,?,?,?)',
            (id,name,age,email,country,id_number)        
        )

def add_teacher(id,name,age,course_teaching,experience, education_level): ##insert data
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO teachers(id,name,age,course_teaching,experience, education_level) VALUES (?,?,?,?,?,?)',
            (id,name,age,course_teaching,experience, education_level)  
        )

def add_course(course_id,name_of_course,subtopics,duration_of_course,field_of_course): ##insert data
    with get_connection() as connection:
        connection.execute(
             'INSERT INTO courses(course_id,name_of_course,subtopics,duration_of_course,field_of_course) VALUES (?,?,?,?,?)',
            (course_id,name_of_course,subtopics,duration_of_course,field_of_course)   
        )

def get_students(): ##get the students
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()
    
def get_teachers(): ##get the teachers
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()
    
def get_courses(): ##get the courses
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()
    