from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

DB_FILE = "exam_db.json"

def read_db():
    if not os.path.exists(DB_FILE):
        return []
    
    with open(DB_FILE,'r') as file:
        return json.load(file)
    
def write_db(data):
    print("------DB Was Just Called--------")
    print("----SAVING TO:", os.path.abspath(DB_FILE))

    with open(DB_FILE,'w') as file:
        return json.dump(data,file,indent=7)
    
class QuestionBlueprint(BaseModel):
    question_id : int
    question_text : str
    answer :  str

@app.post("/add-question")
def add_question(question: QuestionBlueprint):
    print("----Question  was just added..!!!----")
    current_question = read_db()
    new_question_dict={
        "question_id" : question.question_id,
        "question_text" : question.question_text,
        "answer": question.answer
      
    }

    current_question.append(new_question_dict)
    write_db(current_question)
    return {"message":"question added successfully","question":new_question_dict}

@app.get("/get-exam")
def get_single_exam():
    return read_db()


@app.get("/grade-exam/{q_id}/{student_answer}")
def get_grade(q_id,student_answer):
    for question in read_db():
        if question["question_id"] == int (q_id):

            if question["answer"] == student_answer:
                return {"result":"correct!","points": 10}
            else:
                return {"result":"Wrong..!!","Points": 0}
             
    return {"error": "question id not found in the database!"}
