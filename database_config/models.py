from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from database_config.connection import Base
from sqlalchemy.orm import relationship


class Cards(Base):
    __tablename__ = "cards"
    title = Column(String)
    text = Column(String)
    id = Column(Integer, primary_key=True, index=True)