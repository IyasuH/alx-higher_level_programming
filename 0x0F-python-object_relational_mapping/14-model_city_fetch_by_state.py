#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for cityins, stateins in session.query(City,
                                           State).filter(City.state_id
                                                         == State.id).order_by(
                                                             City.id):
        print("{}: ({}) {}".format(stateins.name, cityins.id, cityins.name))

    session.close()


if __name__ == "__main__":
    main()
