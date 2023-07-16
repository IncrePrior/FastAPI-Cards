from pydantic import BaseModel, validator

class User(BaseModel): 
    name: str
    email: str
    password: str
    
    