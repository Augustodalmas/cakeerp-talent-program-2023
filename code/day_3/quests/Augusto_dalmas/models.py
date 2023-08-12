from sqlalchemy import Boolean, ForeignKey,Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Banco

class Item(Banco):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    description = Column(Integer, index=True)
