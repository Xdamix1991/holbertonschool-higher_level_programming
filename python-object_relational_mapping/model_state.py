#!/usr/bin/python3
"""
this module contains the class definition of a State
 """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    class state , inherating from Base
    """
    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return "<State(name='%s')>" % (self.name)
