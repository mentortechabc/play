import sqlite3 as sq

con = sq.connect("local_db.sqlite")
cur = con.cursor()
cur.execute("""    CREATE TABLE IF NOT EXISTS time_slots (
         "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         "start" DATETIME NOT NULL,
         "status" VARCHAR DEFAULT "available"
    );""")
con.close()
