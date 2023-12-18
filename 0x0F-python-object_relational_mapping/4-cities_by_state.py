#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            password=argv[2],
            database=argv[3],
            port=3306
        )

    ptr = db.cursor()

    try:
        ptr.execute("select cities.id, cities.name, states.name from cities\
                inner join states on cities.state_id = states.id\
                order by cities.id asc")
        cities = ptr.fetchall()
        for row in cities:
            print(row)
    except Exception:
        db.rollback()
    ptr.close()
    db.close()
