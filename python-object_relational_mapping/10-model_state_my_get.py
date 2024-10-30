#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
 from the database hbtn_0e_6_usa
 """

from sqlalchemy import func
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    query = session.query(State).filter(
        State.name == sys.argv[4]).order_by(State.id).first()

    if query:
        print("{}".format(query.id))
    else:
        print("Not found")

    session.close()
