import db
from convert_time import convert_from_utc, convert_to_utc_day
from datetime import timedelta, datetime


def get_slots(params):
    """получаем список слотов"""
    if params.week:
        print("week slots: {}".format(params.week))
    if params.day:
        params_start = convert_to_utc_day(params.day)
        params_end = params_start + timedelta(days=1)
        interval = params_start
        while interval < params_end:
            with db.create_connection(params.path) as con:
                cur = con.cursor()

                cur.execute("SELECT * FROM slot WHERE start_interval == (?)", [interval])
            interval += timedelta(minutes=15)
            for result in cur:
                print(convert_from_utc(result))
        # print("day slots: {}".format(params.day))

    if params.filter:
        print("filter: {}".format(params.filter))
