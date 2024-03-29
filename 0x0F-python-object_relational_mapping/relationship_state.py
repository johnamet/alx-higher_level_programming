#!/usr/bin/python3
"""
The module contains a class definition of a State
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


Base = declarative_base()


class State(Base):
    """
    The state class
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)

    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='states', 
            cascade='all, delete')
