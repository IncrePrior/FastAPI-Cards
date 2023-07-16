from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://testdb_c0g2_user:jVJZs7Krg3izvJVUAbZRticKW1JWMXdR@dpg-chnr3iik728jv5d6q3q0-a.frankfurt-postgres.render.com/testdb_c0g2"
            
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
        