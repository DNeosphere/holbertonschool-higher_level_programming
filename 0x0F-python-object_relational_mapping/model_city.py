#!/usr/bin/python3
"""
creates a base class
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

class City(Base):
    """ City class, linked to Cities database """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True,
                nullable=False)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
