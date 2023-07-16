from fastapi import FastAPI, Depends, Request, Form, status, Response, HTTPException
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

@app.get("/card/{id}", status_code=status.HTTP_200_OK)
def getCardById(id, response: Response, db: Session = Depends(get_db)):
    card = db.query(models.Cards).filter(models.Cards.id == id).first()
    if not card: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sorry. There's no card with id {id}.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{"Sorry": f"There's no card with id {id}."}
    
    return card

@app.delete("/card/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteCard(id, db: Session = Depends(get_db)):
    db.query(models.Cards).filter(models.Cards.id == id).delete(synchronize_session=False)
    db.commit()
    return {f"Card with {id} has been deleted."}

@app.put("/card/{id}", status_code=status.HTTP_202_ACCEPTED)
def editCardById(id, card: NewCard, db: Session = Depends(get_db)):
    db.query(models.Cards).filter(models.Cards.id == id).update(request)
    db.commit()
    return 'updated'

# @app.get("/card/{text}")
