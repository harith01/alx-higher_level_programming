#!/usr/bin/python3
"""Write a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa"""

if __name__ == "__main__":
    import sys
    from relationship_state import State, Base
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(City(name='San Francisco', state=State('California')))
    session.commit()
    session.close()
