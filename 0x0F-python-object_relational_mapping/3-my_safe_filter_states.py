#!/usr/bin/python3
"""A script that takes in an argument
   and displays all values in the states table
   from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
