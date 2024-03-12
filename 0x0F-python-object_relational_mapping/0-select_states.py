#!/usr/bin/python3
"""
Script to list all states from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=awd[2], db=argv[3], charset="utf8")
    cursor = db.cursor
