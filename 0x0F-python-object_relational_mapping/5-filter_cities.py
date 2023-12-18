#!/usr/bin/python3
"""This script takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    try:
        db = MySQLdb.connect(
                host='localhost',
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                port=3306
            )

        ptr = db.cursor()

        ptr.execute("select cities.id, cities.name, states.name from cities \
                inner join states on cities.state_id = states.id where \
                states.name like binary %s order by cities.id asc",
                    (argv[4],))

        rows = ptr.fetchall()
        for row in rows:
            print(row[1], end=", " if row != rows[-1] else "")
        print()
    except Exception as err:
        db.rollback()
        print("MySQL Error {}: {}".format(err.args[0], err.args[1]))

    finally:
        if 'ptr' in locals() or 'ptr' in globals():
            ptr.close()
        if 'db' in locals() or 'db' in globals():
            db.close()
