from pydantic import BaseModel, validator

class Card(BaseModel):
    text: str
    class Config():
        orm_mode = True
    
    @validator('text')
    def check_for_max_300_chars(cls, v):
            if len(v) > 300 : 
                raise ValueError('Great that you max out 300 characters in this note. To continue, start a new note.')
            return v