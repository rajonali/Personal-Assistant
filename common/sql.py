#Retrieve already made sql script from botnet project later if needed.
import os,sys

sys.path.append("C:\\Users\\ta044\\Documents\\Tasnim Projects\\BOOPT")

import sqlite3
from app.common.formatting import colors 

def conn_db(filepath):
    try:
        # set the database connectiont to autocommit w/ isolation level
        conn = sqlite3.connect(filepath)
        #conn.text_factory = str
        return conn

    except Exception:
        print(colors.red + "[!] Could not connect to database" + colors.ENDC)
        print(colors.red + "[!] Please run setupdbs.py" + colors.ENDC)
        sys.exit()


def execute_query(conn, query, args=None):
    cur = conn.cursor()
    if args:
        cur.execute(query, args)
    else:
        cur.execute(query)
    results = cur.fetchall()
    return results
    

