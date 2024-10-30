#!/usr/bin/python3
"""
this module contains a script that prints the first State object
from the database hbtn_0e_6_usa

 """
import sys
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.id.like('1'))
    for row in query.all():
        print("%s: %s" % (row.id, row.name))

    session.close()
