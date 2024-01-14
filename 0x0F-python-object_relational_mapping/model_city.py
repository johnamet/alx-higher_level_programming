#!/usr/bin/python3
"""
The script contains the class definition for city
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from model_state import Base


class City(Base):
    """
    The class defines the city entity
    """

    __tablename__ = "cities"

    id = Column(Integer, nullable=False,
                primary_key=True,
                autoincrement=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
