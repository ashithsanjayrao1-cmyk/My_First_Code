from fastapi import FastAPI
from pydantic import BaseModel
import os
import json

app = FastAPI()

DB_FILE = "workouts.json"

def read_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE,'r') as file:
        return json.load(file)
    
def write_db(data):
    print("-----db was just called---")
    print("---saving to ---:",os.path.abspath(DB_FILE))

    with open(DB_FILE,'w') as file:
        return json.dump(data,file,indent= 5)
    

class WorkoutBlueprint(BaseModel):
    workout_id : int
    exercise : str
    duration_minutes : int
    calories_burned : int

@app.post("/log-workout")
def add_workout(workout : WorkoutBlueprint):
    print("----Workout Just Addded---")
    current_workout = read_db()
    new_current_workout = {
        "workout_id" : workout.workout_id,
        "exercise" : workout.exercise,
        "duration"  : workout.duration_minutes,
        "calories" : workout.calories_burned
    }
    current_workout.append(new_current_workout)
    write_db(current_workout)

    return { "message":"Workout saved successfully!","Workout": new_current_workout}

@app.get("/history")
def get_all_history():
    return read_db()

@app.get("/total-calories")
def get_calories():
    total = 0
    for workout in read_db():
            total = total + workout["calories"]
       

    
    return {"message": "Great Job", "total_calories_burned" : total }
        
    