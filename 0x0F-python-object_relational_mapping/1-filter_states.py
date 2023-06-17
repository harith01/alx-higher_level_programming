#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    [print(row) for row in rows if row[1][0] == "N"]
