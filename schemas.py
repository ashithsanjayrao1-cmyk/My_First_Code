from pydantic import BaseModel

class TaskCreate(BaseModel):
    title : str
    is_completed : bool = False