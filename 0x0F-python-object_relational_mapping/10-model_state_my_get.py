#!/usr/bin/python3
"""
The script prints the State object with the name
passed as argument from the database
"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://\
                           {}:{}@localhost:3306/{}'.
                           format(user, passwd, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name, state_name)\
        .first()
    
    if query is None:
        print("Not found")
    else:
        print(query.id)
