#!/usr/bin/python3
"""a script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).filter(State.name == "{}".format(sys.argv[4]))
    found = False
    for row in rows:
        if (row.name == sys.argv[4]):
            print(row.id)
            found = True
            break
    if (found is False):
        print("Not found")
    session.close()
