from fastapi import FastAPI, Depends, Request, Form, status
from pydantic import BaseModel
from database_config.connection import Base, engine, get_db
from database_config import models
from sqlalchemy.orm import Session

from schemas.CardsSchemas import NewCard

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"welcome": "Hi. So good to see you here."}

@app.post("/card")
def newCard(card: NewCard, db: Session = Depends(get_db)):
    new_card = models.Cards(title=card.title, text=card.text)    
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

@app.get("/card")
def allCards(db: Session = Depends(get_db)):
    cards = db.query(models.Cards).all()
    return cards

@app.get("/card/{id}")
def getCardById(id, db: Session = Depends(get_db)):
    card = db.query(models.Cards).filter(models.Cards.id == id).first()
    return card