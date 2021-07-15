import db

def create_test_table(params):
    con = db.create_connection(params.path)
    db.create_slots_table(con)
    db.create_admininfo_table(con)
    db.create_bookinginfo_table(con)


def clean_table_slots(params):
    with db.create_connection(params.path) as con:
            cur = con.cursor()
            cur.execute("""DROP TABLE IF EXISTS Slots;""")


def get_test_slots(params):
    with db.create_connection(params.path) as con:
            cur = con.cursor()
            a = cur.execute(
                "SELECT * FROM Slots")
            return a.fetchall()