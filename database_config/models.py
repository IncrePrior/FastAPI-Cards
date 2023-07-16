from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from database_config.connection import Base
from sqlalchemy.orm import relationship


class Cards(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    
class Users(Base): 
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)