#!/usr/bin/python3
"""A script that lists all cities
   from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = """SELECT cities.id, states.name, cities.name
             FROM cities LEFT JOIN states
	     ON cities.state_id = states.id"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
