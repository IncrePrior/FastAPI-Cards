from pydantic import BaseModel, validator

class NewCard(BaseModel):
    title: str
    text: str
    
