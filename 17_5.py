from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

DB_FILE = "library.json"

def read_db():
    if not os.path.exists(DB_FILE):
        return[]
    
    with open(DB_FILE,'r') as file:
        return json.load(file)
    
def write_db(data):
    print("------DB Was Just Called--------")
    print("------Saviong File To:",os.path.abspath(DB_FILE))
    
    with open(DB_FILE,'w') as file:
        return json.dump(data,file,indent=7)
    
class BookBlueprint(BaseModel):
    title : str
    author : str
    pages : int


@app.get("/")
def home_page():
    return "Welcome to DIGITAL LIBRARY API"

@app.get("/books")
def get_all_books():
    return read_db()

@app.post("/add-book")
def add_book(book: BookBlueprint):
    print("----ADD WAS JUST TRIGGERED..!!!----")
    current_books = read_db()
    new_book_dict ={
        "title" : book.title,
        "author" : book.author,
        "pages" : book.pages 

    }
    current_books.append(new_book_dict)
    write_db(current_books)

    return {"message": "Task Saved Successfully","task": new_book_dict}

@app.get("/books/{author_name}")
def get_single_book(author_name):
    for author in read_db():
        if author["author"] == author_name:
            return author
        

    return {"author":"author not found..!!"}
    
