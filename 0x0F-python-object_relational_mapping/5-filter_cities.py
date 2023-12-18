#!/usr/bin/python3
"""This script takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
        )

    ptr = db.cursor()

    try:
        ptr.execute("select name from cities where state_id=(select id from \
                    states where name like binary %s) order by cities.id \
                    asc", (argv[4],))
        rows = ptr.fetchall()
        i = 0
        for row in rows:
            for letter in row:
                print(letter, end='')
                if i < len(rows) - 1:
                    print(", ", end='')
            i += 1
    except Exception:
        db.rollback()

    ptr.close()
    db.close()
