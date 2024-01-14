#!/usr/bin/python3
"""
Creates the state california with city san francisco
"""
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
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

    queries = session.query(State)\
        .order_by(State.id).group_by(State.id).all()
    
    for query in queries:
        print("{}: {}".format(query.id, query.name))
        for city in query.cities:
            print("\t {}: {}".format(city.id, city.name))
