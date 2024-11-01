#!/usr/bin/python3
"""
this module contains the class definition of a cities
 """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model_state import Base, State

class City(Base):
    """
    class cities inherating from base
      """
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

