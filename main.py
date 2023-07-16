from fastapi import FastAPI, Depends, Request, Form, status, Response, HTTPException
from pydantic import BaseModel
from database_config.connection import Base, engine, get_db
from database_config import models
from sqlalchemy.orm import Session

from schemas.CardsSchemas import Card
from schemas.UserSchemas import User, ShowUser

models.Base.metadata.create_all(bind=engine)

description = """
Cards Against Negativity helps you beat self-doubt and builds positive vibes.

You will be able to: 
- create cards with positive vibes
- read cards and remember how wonderful you are
"""

app = FastAPI(
    title = "Cards Against Negativity",
    description = description
    summary = "An app to fight self-doubt and negative thoughts.",
    contact = {
        "name" : "Val the OCD coder", 
        "URL" : "cardsagainstnegativity.com" 
        "email" : "negativenomore@positivevibesonly.co.uk"}
    )

@app.get("/")
def home():
    return {"Message": "Hi. So good to see you here."}

@app.post("/card", response_model=Card, tags=['cards'])
def newCard(card: Card, db: Session = Depends(get_db)):
    new_card = models.Cards(title=card.title, text=card.text)    
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

@app.get("/card", tags=['cards'])
def allCards(db: Session = Depends(get_db)):
    cards = db.query(models.Cards).all()
    return cards

@app.get("/card/{id}", status_code=status.HTTP_200_OK, tags=['cards'])
def getCardById(id: int, response: Response, db: Session = Depends(get_db)):
    card = db.query(models.Cards).filter(models.Cards.id == id).first()
    if not card: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find card with id {id}.")
    return card

# TypeError: Failed to execute 'fetch' on 'Window': Request with GET/HEAD method cannot have body.
@app.get("/card/{text}", tags=['cards'])
def getCardByText(text: str, card: Card, db: Session = Depends(get_db)):
    for text in Cards: 
        if text not in Cards: 
            return {'Message':f"Can't find card with text {text}"}
    
            if Cards[id]["text"] == text.lower():
                return Cards[id]
    
# internal server error 500 on Swagger UI 
@app.put("/card/{id}", tags=['cards'])
def editCardById(id: int, card: Card, db: Session = Depends(get_db)):
    if id not in Cards:
        return {'Message': f'Card ID {id} not found.'}
    if card.title != None: 
        Cards[id].title = card.title
    if card.text != None:
        Cards[id].text = card.text
    return Cards[id]

# internal server error 500 on Swagger UI 
@app.delete("/card/{id}", tags=['cards'])
def deleteCardById(id: int, db: Session = Depends(get_db)):
    if id not in Cards: 
        return {"Message": f"Sorry. Card ID {id} doesn't exist."}
    del Cards[id]
    return {"Message": f"Card ID {id} deleted."}

# internal server error 500 on Swagger UI but entries are registered on PgAdmin
@app.post("/user", response_model=ShowUser, tags=['users'])
def addUser(user: ShowUser, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name, email=user.email)    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# internal server error 500 on Swagger UI 
@app.get("/user/{user_id}", response_model=ShowUser, tags=['users'])
def getUserById(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find user with id {user_id}.")
    return user

