#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
