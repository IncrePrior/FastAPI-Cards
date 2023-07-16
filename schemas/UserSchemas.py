from pydantic import BaseModel, validator

class User(BaseModel): 
    name: str
    email: str
    password: str
    
@validator('name')
def check_for_max_300_chars(cls, v):
        if len(v) > 300 : 
            raise ValueError('Maximum 300-character limit for name.')
        return v
    
@validator('password')
def check_for_min_10_chars(cls, v):
        if len(v) < 10 : 
            raise ValueError('Please create a password of at least 10 characters.')
        return v