#!/usr/bin/python3
""" almost forgot how to comment """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN\
    states ON cities.state_id = states.id WHERE states.name = '{}'\
    ORDER BY cities.id".format(argv[4]))
    cityz = cur.fetchall()
    print(", ".join([row[0] for row in cityz]))
    cur.close()
    db.close()
