#!/usr/bin/python3
"""
a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """
    And this function deletes a rows with name conating letter 'a'
    using SQLAlchemy ORM
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.
                                                  id).filter(State.
                                                             name.
                                                             contains('a')):
        session.delete(instance)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
