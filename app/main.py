from fastapi import FastAPI
from pydantic import BaseModel
from database import create_table,add_student,get_students,add_teacher,get_teachers,add_course,get_courses 

app = FastAPI()
create_table()

class Student(BaseModel):
    id: int
    name:str
    age:int
    email:str
    country:str
    id_number:int


students = []


class Teacher(BaseModel):
    id : int
    name:str
    age:int
    email:str
    course_teaching : str
    experience : int 
    education_level :str

teachers = []


class Course(BaseModel):
    course_id: int
    name_of_course:str
    subtopics : str
    duration_of_course:int
    field_of_course : str


courses = []


@app.get("/")
def home():
    return {"message":"Welcome to my API Server Sumaya"}

@app.get("/students")
def list_students():
    students = get_students()
    return students

def register_student(student:Student):
    add_student(student.id,student.name,student.age,student.email,student.country,student.id_number)
    return student


@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"message":"Student registered","student":student}

@app.get("/teachers")
def list_teachers():
    teachers = get_teachers()
    return teachers

def register_teacher(teacher:Teacher):
    add_teacher(teacher.name,teacher.age,teacher.email,teacher.course_teaching,teacher.experience,teacher.education_level)
    return teacher


@app.post("/teachers")
def create_teacher(teacher: Teacher):
    teachers.append(teacher)
    return {"message":"Teacher registered","teacher":teacher}

@app.get("/courses")
def list_courses():
    courses = get_courses()
    return courses

def courses_available(course:Course):
    add_course(course.course_id,course.name_of_course,course.subtopics,course.duration_of_course,course.field_of_course)
    return course


@app.post("/courses")
def create_courses(course: Course):
    courses.append(course)
    return {"message":"Courses Available","course":course}




