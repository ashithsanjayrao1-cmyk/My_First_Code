# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def home_page():
#     return {"message":"Welcome to the real world. My server is alive!"}


from fastapi import FastAPI

app = FastAPI()

classroom = [
    {"name": "Ashith","subject": "python","score":95},
    {"name": "Rahul","subject": "java","score":80},
    {"name": "Priya","subject": "english","score":92}
]

@app.get("/students")
def get_all_students():
    return classroom

@app.get("/students/{student_name}")
def get_single_student (student_name):

    for student in classroom:
        if student["name"] == student_name:
            return student
        
    return {"Error":"Student not found"}