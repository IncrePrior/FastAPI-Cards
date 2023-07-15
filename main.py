from fastapi import FastAPI, Depends, Request, Form, status, Response
from pydantic import BaseModel
from database_config.connection import Base, engine, get_db
from database_config import models
from sqlalchemy.orm import Session

from schemas.CardsSchemas import NewCard

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"Welcome": "Hi. So good to see you here."}

@app.post("/card", status_code=status.HTTP_201_CREATED)
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

@app.get("/card/{id}", status_code=200)
def getCardById(id, response: Response, db: Session = Depends(get_db)):
    card = db.query(models.Cards).filter(models.Cards.id == id).first()
    if not card: 
        response.status_code = status.HTTP_404_NOT_FOUND
        return{"Sorry": f"There's no card with id {id}."}
    
    return card

# @app.get("/card/{text}")
# @app.delete("/")
# @app.put("/card")