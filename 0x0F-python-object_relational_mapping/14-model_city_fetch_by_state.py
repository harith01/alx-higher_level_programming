#!/usr/bin/python3
"""A script that prints all City objects
from the database hbtn_0e_14_usa"""

if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).select_from(State).join(City)
    for q in query:
        print("{}: ({}) {}".format(q[0].name, q[1].id, q[1].name))
