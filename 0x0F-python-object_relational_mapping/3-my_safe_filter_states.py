#!/usr/bin/python3
"""This script takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But safe from MySQL injections!
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
        )

    ptr = db.cursor()

    try:
        ptr.execute("select * from states where states.name like binary %s\
                order by states.id asc", (argv[4],))
        rows = ptr.fetchall()
        for row in rows:
            print(row)
    except Exception:
        db.rollback()

    ptr.close()
    db.close()
