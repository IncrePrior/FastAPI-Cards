from pydantic import BaseModel, validator

class Card(BaseModel):
    title: str
    text: str
    author_id: int
    class Config():
        orm_mode = True
    
@validator('title')
def check_for_max_80_chars(cls, v):
        if len(v) > 80 : 
            raise ValueError('Fab that you max out 80 characters for a title. There is more space for you to continue in the note.')
        return v
    
@validator('text')
def check_for_max_300_chars(cls, v):
        if len(v) > 300 : 
            raise ValueError('Great that you max out the 250 characters in this note. If you need more space, continue on a new note.')
        return v