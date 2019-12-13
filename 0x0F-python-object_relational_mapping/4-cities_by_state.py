#!/usr/bin/python3
"""
Selects all states from a db
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="127.0.0.1", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("\
    SELECT cities.id, cities.name, states.name \
    FROM cities\
    INNER JOIN states\
    ON cities.state_id = states.id\
    ORDER BY cities.id ASC;")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
