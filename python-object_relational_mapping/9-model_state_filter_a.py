#!/usr/bin/python3
"""
script that lists all State objects that contain the letter 'a'
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

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(
        State.name.like('%a')).order_by(State.id)
    rows = query.all()
    if rows:
        for row in rows:
            print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")

    session.close()
