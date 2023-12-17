#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    myconn = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306
        )
    cur = myconn.cursor()

    try:
        cur.execute("select * from states order by id asc")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception:
        myconn.rollback()

    cur.close()
    myconn.close()
