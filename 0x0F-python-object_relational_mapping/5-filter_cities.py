#!/usr/bin/python3
"""A script that takes in the name of a state as
   an argument and lists all cities of that state
   using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
             FROM cities LEFT JOIN states
	     ON cities.state_id = states.id WHERE states.name = %s;"""
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[1] for row in rows]))   
