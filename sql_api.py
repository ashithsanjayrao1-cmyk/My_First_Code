from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import schemas
from database import engine ,sessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"],
)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally :
        db.close()

@app.post("/add-task")
def add_task(task : schemas.TaskCreate, db: Session = Depends(get_db)):
    new_db_task = models.DBTASK(
        title = task.title,
        is_completed = task.is_completed
    )
    db.add(new_db_task)

    db.commit()

    db.refresh(new_db_task)

    return {"message":"Saved to SQL Database!","task":new_db_task}

@app.get("/")
def home():
    return {"message": "SQL Database is alive and running"}

@app.get("/tasks")
def get_all_tasks(db: Session = Depends(get_db)):
    all_tasks = db.query(models.DBTASK).all()

    return all_tasks

@app.delete("/delete-task/{task_id}")
def delete_task(task_id: int,db: Session = Depends(get_db)):
    task_to_delete = db.query(models.DBTASK).filter(models.DBTASK.id == task_id).first()

    if task_to_delete is None:
        return {"error": "Task not found! It might have already been deleted."}
    
    db.delete(task_to_delete)

    db.commit()

    return {"message":f"Task{task_id} has been successfully deleted."}