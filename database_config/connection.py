from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://caidb_user:gloUA0PtjtltiZLTlukT8IEBkNxeQxx8@dpg-cj0e6ns07spl5oop44vg-a.frankfurt-postgres.render.com/caidb"
            
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
        