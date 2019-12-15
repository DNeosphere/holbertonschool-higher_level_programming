#!/usr/bin/python3
"""
creates a base class
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.like(sys.argv[4])).all()
    if state:
        print("{}".format(state[0].id))
    else:
        print("Not found")
    session.close()
