#!/usr/bin/python3
""" almost forgot how to comment """


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    sesh = Session()
    newstatename = State(name="Louisiana")
    sesh.add(newstatename)
    sesh.commit()
    print(newstatename.id)
    sesh.close()
