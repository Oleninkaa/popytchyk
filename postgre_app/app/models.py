from importlib import metadata
from sqlalchemy import MetaData, String, Boolean, Integer, Column, text, TIMESTAMP, DateTime
from sqlalchemy.orm import registry

from database import Base

metadata = MetaData()

class Trip(Base):
    __tablename__='trips'

    metadata,
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(15), nullable=False)  
    email = Column(String(100), nullable=False)
    start = Column(String, nullable=False)
    finish = Column(String, nullable=False)
    date = Column(String, nullable=False)
    comment = Column(String, nullable=True)
    
