from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

DB_FILE = "ashith.json"

def read_db():
    if not os.path.exists(DB_FILE):
        return[]
    
    with open(DB_FILE,"r") as file:
        return json.load(file)
    
def write_db(data):
    print("🚨🚨🚨 write_db WAS JUST CALLED! 🚨🚨🚨")
    print("🚨 SAVING FILE TO:", os.path.abspath(DB_FILE))
    with open(DB_FILE,"w") as file:
        json.dump(data,file,indent=4)

class TaskBlueprint(BaseModel):
    title: str
    is_completed :bool

@app.get("/")
def get_home_page():
    return "Welcome to the page which u want to know the task cpmpleted or not"
    

@app.get("/tasks")
def get_all_tasks():
    return read_db()

@app.post("/add-task")
def add_task(task: TaskBlueprint):
    print("🚨 TRIGGER ALERT: POST ROUTE WAS JUST HIT! 🚨")
    current_tasks = read_db()

    new_task_dict = {
        "title": task.title,
        "is_completed": task.is_completed
    }

    current_tasks.append(new_task_dict)

    write_db(current_tasks)

    return {"message":"Task permanently saved!","task":new_task_dict}

@app.get("/tasks/{task_title}")
def get_single_task(task_title):
    for tasks in read_db():
        if tasks["title"] == task_title:
            return tasks
    
    return {"error":"Task Not Found..!"}