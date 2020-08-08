#!/usr/bin/python3
""" almost forgot how to comment """


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    sesh = Session()
    for city, state in sesh.query(City, State).join(State).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    sesh.close()
