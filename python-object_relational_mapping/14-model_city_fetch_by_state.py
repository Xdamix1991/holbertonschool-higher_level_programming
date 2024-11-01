#!/usr/bin/python3
"""
this module contains a script that
 prints all City objects from the database hbtn_0e_14_usa
 """
import sys
from model_city import City
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import select, join

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    stm_1 = select(City.id.label("city_id"), City.name.label("city_name"),
                   City.state_id).subquery()

    stm = select(State.name, stm_1.c.city_id, stm_1.c.city_name).join(
        stm_1, State.id == stm_1.c.state_id).order_by(stm_1.c.city_id)

    # print (stm)
    # on imprime l'equivalant en commande sql pour sortir les alias
    # // lien de docs:
    # https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html#joins//

    # NB si les alias autogénérés ne sont pas acessible
    # on peut les rajouter manuelement
    # avec .label("alias")
    """ SELECT states.name, anon_1.id, anon_1.name AS name_1
    FROM states JOIN (
    SELECT cities.id AS id, cities.name AS name, cities.state_id AS state_id
    FROM cities) AS anon_1 ON states.id = anon_1.state_id
    """

    # les alias seront utilisés pour l impression

    for row in session.execute(stm):
        print("{}: ({}) {}".format(row.name, row.city_id, row.city_name))
    session.close()

    """

    vesion 2 bcp plus simmple
    results = session.query(State, City).join(
    City, State.id == City.state_id).order_by(City.id)
    for state, city in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    """
