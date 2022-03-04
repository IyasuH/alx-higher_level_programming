#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    n = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst in session.query(State).filter(State.name == sys.argv[4]):
        n = 1
    if (n == 1):
        print("{}".format(inst.id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
