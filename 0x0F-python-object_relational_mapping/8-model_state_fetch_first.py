#!/usr/bin/python3
"""
The scripts prints the first State objct from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqlconnector://{}:\
                           {}@localhost:3306/{}'
                           .format(user, passwd, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print()
    else:
        print("{}: {}".format(first_state.id, first_state.name))