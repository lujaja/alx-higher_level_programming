#!/usr/bin/python3
"""This script lists all states with name starting with N (upper N) from db
hbtn_0e_0_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            password=argv[2],
            database=argv[3],
            port=3306
        )

    ptr = db.cursor()

    try:
        ptr.execute("select * from states where name like 'N%'order by id asc")
        rows = ptr.fetchall()
        for row in rows:
            print(row)
    except Exception:
        db.rollback()

    ptr.close()
    db.close()
