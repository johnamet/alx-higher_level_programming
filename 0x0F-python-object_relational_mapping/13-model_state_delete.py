#!/usr/bin/python3
"""
The script adds the State object Louisiana to the database
"""
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine, text
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:\
                           {}@localhost:3306/{}'
                           .format(user, passwd, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).filter(State.name.like('%a%')).all()

    rows.delete()

    session.commit()
