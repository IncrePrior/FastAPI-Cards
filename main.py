from fastapi import FastAPI, Depends, Request, Form, status, Response, HTTPException
from pydantic import BaseModel
from database_config.connection import Base, engine, get_db
from database_config import models
from sqlalchemy.orm import Session

from schemas.CardsSchemas import Card

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"Message": "Hi. So good to see you here."}

@app.post("/card", response_model=Card)
def newCard(card: Card, db: Session = Depends(get_db)):
    new_card = models.Cards(title=card.title, text=card.text)    
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

@app.get("/card")
def allCards(db: Session = Depends(get_db)):
    cards = db.query(models.Cards).all()
    return cards

@app.get("/card/{id}", status_code=status.HTTP_200_OK)
def getCardById(id: int, response: Response, db: Session = Depends(get_db)):
    card = db.query(models.Cards).filter(models.Cards.id == id).first()
    if not card: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find card with id {id}.")
    return card

# TypeError: Failed to execute 'fetch' on 'Window': Request with GET/HEAD method cannot have body.
@app.get("/card/{text}")
def getCardByText(text: str, card: Card, db: Session = Depends(get_db)):
    for text in Cards: 
        if text not in Cards: 
            return {'Message':f"Can't find card with text {text}"}
    
            if Cards[id]["text"] == text.lower():
                return Cards[id]
    
# internal server error 500 on Swagger UI 
@app.put("/card/{id}")
def editCardById(id: int, card: Card, db: Session = Depends(get_db)):
    if id not in Cards:
        return {'Message': f'Card ID {id} not found.'}
    if card.title != None: 
        Cards[id].title = card.title
    if card.text != None:
        Cards[id].text = card.text
    return Cards[id]

# internal server error 500 on Swagger UI 
@app.delete("/card/{id}")
def deleteCardById(id: int, db: Session = Depends(get_db)):
    if id not in Cards: 
        return {"Message": f"Sorry. Card ID {id} doesn't exist."}
    del Cards[id]
    return {"Message": f"Card ID {id} deleted."}
