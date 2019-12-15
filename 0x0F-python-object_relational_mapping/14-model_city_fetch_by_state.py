#!/usr/bin/python3
"""
creates a base class
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City)\
                              .filter(State.id == City.state_id)\
                              .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
