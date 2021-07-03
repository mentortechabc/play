import sqlite3 as sq

with sq.connect("local_db2.sqlite") as con:
    cur = con.cursor()
    res = cur.execute("DROP TABLE IF EXISTS time_slots")
    cmd_create = """    CREATE TABLE IF NOT EXISTS time_slots (
         "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         "start" DATETIME NOT NULL,
         "status" VARCHAR DEFAULT "available"
    );"""
    res = cur.execute(cmd_create)
    print(res)

    cmd_insert = """INSERT INTO time_slots(id, start, status) 
    VALUES 
	(1, "2020-01-01 20:20", "available"),
	(2, "2020-02-02 20:20", "available"),
	(3, "2020-03-03 20:20", "booked")
	;
    """
    # res = cur.execute(cmd_insert)
    try:
        res = cur.execute(cmd_insert)
    except sq.IntegrityError as e:
        print("something went wrong with the integrity:")
        print(e)
    else:
        print(res)


    cmd_select = """SELECT * FROM time_slots;"""
    res = cur.execute(cmd_select)
    for row in res:
        print(row)