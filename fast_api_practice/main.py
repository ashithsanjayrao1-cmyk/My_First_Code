from fastapi import FastAPI ,HTTPException,Depends
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models




app = FastAPI()

models.Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/")
# def home():
#     return {"message":"Welcome to my brand new server"}


# @app.get("/users/{ashith}")
# def get_user_profile(ashith):
#     return {"message": f" Hello {ashith}, here is your profile data"}


# @app.get("/items/{item_id}")
# def get_all_item(item_id):
#     return {"requested_item": item_id , "status":"In stock"}


# @app.get("/inventory")
# def get_inventory(limit: int = 10):
#     return {"message": f"Returning {limit} items from the database!!"}


# @app.get("/search")
# def get_search_items(q: str):
#     return {"Search": q , "results": "Found 5 Matching item"}

class UserAccount(BaseModel):
    username : str
    email : str



@app.post("/signup")
def create_user(account : UserAccount ,db: Session = Depends(get_db)):
    new_db_user = models.User(username = account.username , email = account.email)

    db.add(new_db_user)

    db.commit()

    db.refresh(new_db_user)

    return {"message":f"Successfuly save {new_db_user} to the dataabase..!!"}

@app.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    
    # Go to the User table, query it, and grab ALL rows!
    users = db.query(models.User).all()
    
    return {"total_users": len(users), "users": users}

# taken_users = ["ashith","admin","rohan"]

# @app.post("/signup")
# def create_user(user_name: UserAccount):
#     if user_name.username in taken_users:
#         raise HTTPException(status_code=400 , detail="username already taken!")
    

#     return {"message": f"Account created for {user_name}!","email_saved":user_name.email}

# class Product(BaseModel):
#     name : str
#     price: float


# @app.post("/add-product")
# def add_new_products(item : Product):
#     return {"message": f"Successfully added {item.name} for ${item.price}"}

# @app.get("/secret-club")
# def secret_club(password : str):
#     if password != "batman":
#         raise HTTPException(status_code= 400, detail ="wrong password,Get Out!!!")
    
#     return {"message":"Welcomne to the batcave"}

def verify_token(token: str):
    if token != "super-secret-key":
        raise HTTPException(status_code=401,detail="invalid token!!!!!!")
    return {"message":"VALID TOKEN COME IN"}


@app.get("/vault")
def open_vault(is_approved: bool = Depends(verify_token)):
    return {"Message":"Welcome to the secreat vault. Here is one million dollars."}

def check_pin(pin: int):
    if pin != 1234:
        raise HTTPException(status_code=401,detail="Wrong Pin!")
    
    return True

@app.get("/balance")
def get_balance(approved : bool  = Depends(check_pin)):
    return {"balance": "$5000"}