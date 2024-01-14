#!/usr/bin/python3
"""
The scripts lists all objects that
contain letter a from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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

    rows = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    for row in rows:
        print("{}: {}".format(row.id, row.name))
