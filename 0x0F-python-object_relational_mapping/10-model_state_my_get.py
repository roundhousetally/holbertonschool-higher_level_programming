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
    sesh = Session()
    injectfree = argv[4]
    statesearch = sesh.query(State).filter_by(name=injectfree).first()

    if statesearch is None:
        print("Not Found")
    else:
        print("{}".format(statesearch.id))
    sesh.close()
