import os
import sqlite3

dir_name = os.path.dirname(__file__)
path_to_db = os.path.join(dir_name, "../../calendar-admin/main_db.sqlite")


def query_db():
    connection = sqlite3.connect(path_to_db)
    result = []

    for booking in connection.execute("SELECT * FROM BookingInfo"):
        result.append(booking)

    connection.close()

    return result