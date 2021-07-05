import sqlite3 as sq
from datetime import timedelta, datetime


def get_slots(namespace):
    """получаем список слотов"""
    if namespace.week:
        print("week slots: {}".format(namespace.week))
    if namespace.day:
        namespace_start = datetime.strptime(namespace.day, "%Y-%m-%d")
        namespace_end = namespace_start + timedelta(days=1)
        interval = namespace_start
        while interval < namespace_end:
            with sq.connect('database.db') as con:
                cur = con.cursor()

                cur.execute("SELECT * FROM slot WHERE start_interval == (?)", [interval])
            # print(interval)
            interval += timedelta(minutes=15)
            for result in cur:
                print(result)
        print("day slots: {}".format(namespace.day))

    if namespace.filter:
        print("filter: {}".format(namespace.filter))
