#!/usr/bin/python3
"""
script that changes the name of a State object
from the database hbtn_0e_6_usa
 """
from sqlalchemy import func
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import delete

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    stmt = (
        delete(State).
        where(State.name.like('%a'))
    )

    session.execute(stmt)
    session.commit()

    session.close()
