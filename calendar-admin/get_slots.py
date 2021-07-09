import sqlite3 as sq
from datetime import timedelta, datetime


def get_slots(params):
    """получаем список слотов"""
    if params.week:
        print("week slots: {}".format(params.week))
    if params.day:
        namespace_start = datetime.strptime(params.day, "%Y-%m-%d")
        namespace_end = namespace_start + timedelta(days=1)
        interval = namespace_start
        while interval < namespace_end:
            with sq.connect(params.path) as con:
                cur = con.cursor()

                cur.execute("SELECT * FROM slot WHERE start_interval == (?)", [interval])
            # print(interval)
            interval += timedelta(minutes=15)
            for result in cur:
                print(result)
        print("day slots: {}".format(params.day))

    if params.filter:
        print("filter: {}".format(params.filter))
