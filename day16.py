from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

classroom = [
    {"name":"Ashith","subject":"python","score":95},
    {"name": "Rahul","subject": "java","score":80},
    {"name": "Priya","subject": "english","score":92}
]

@app.get("/students")
def get_all_students():
    return classroom

@app.get("/student/{student_name}")
def get_single_student(student_name):
    for student in classroom:
        if student["name"] == student_name:
            return student
    return{"Error":"student not found"}

class StudentBlueprint(BaseModel):
    name: str
    subject: str
    score: int

@app.post("/add-student")
def add_new_student(student: StudentBlueprint):
    new_student_dict = {
        "name": student.name,
        "subject": student.subject,
        "score": student.score
    }

    classroom.append(new_student_dict)

    return{"message":"Student successfully added!","new_student": new_student_dict}