#!/usr/bin/python3
"""
Selects all states from a db
"""
if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states \
    WHERE name = %(state_name)s \
    ORDER BY states.id ASC;", {'state_name': argv[4]})
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
