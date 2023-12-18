#!/usr/bin/python3
"""This script takes an argument and displays all values in the ststes table
of hbtn_0e_0_usa matches the argument
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
        ptr.execute("select * from states where states.name like binary '{}'\
                order by states.id asc".format(argv[4]))

        rows = ptr.fetchall()

        for row in rows:
            print(row)
    except Exception:
        db.rollback()

    ptr.close()
    db.close()
