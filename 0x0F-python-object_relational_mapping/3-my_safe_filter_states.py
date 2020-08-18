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
    cur.execute("SELECT * FROM `states`")
    states = cur.fetchall()
    for state in states:
        if state[1] == argv[4]:
            print(state)
    cur.close()
    db.close()
