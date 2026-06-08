from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

task_db = [
    {"title":"Python","is_completed":"true"},
    {"title":"Java","is_completed":"false"},
    {"title":"Java Script","is_completed":"true"}


]

class TaskBlueprint(BaseModel):
    title : str
    is_completed : bool

@app.get("/tasks")
def get_all_tasks():
    return task_db

@app.post("/add-task")
def add_task(task: TaskBlueprint):
    new_task_dict = {
        "title": task.title,
        "is_completed": task.is_completed

    }
    task_db.append(new_task_dict)
    return{"message":"tasks successfully added!","new_task": new_task_dict}


@app.get("/tasks/{task_title}")
def get_single_task(task_title):
    for tasks in task_db:
        if tasks["title"] == task_title:
            return tasks
    
    return {"error":"Task Not Found..!"}


    
