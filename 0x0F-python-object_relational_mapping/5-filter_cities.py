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
    SELECT cities.name\
    FROM cities\
    INNER JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name = %(c_name)s\
    ORDER BY cities.id ASC;", {'c_name': argv[4]})

    states = cur.fetchall()

    ciudades = []

    for item in rows:
        ciudades.append(item[0])

    lista = ", ".join(ciudades)
    print(lista)

    cur.close()
    db.close()
