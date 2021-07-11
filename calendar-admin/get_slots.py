import db
from convert_time import convert_from_utc, convert_to_utc_day, collapse_intervals
from datetime import timedelta


def get_slots(params):
    """получаем список слотов"""
    lst = []
    if params.week:
        params_start = convert_to_utc_day(params.week)
        params_end = params_start + timedelta(days=8)
        interval = params_start

        while interval < params_end:
            with db.create_connection(params.path) as con:
                cur = con.cursor()

                if params.filter:
                    if params.filter == "free":
                        cur.execute("SELECT start_interval FROM Slots "
                                    "WHERE start_interval == (?) AND booking_id is null", [interval])
                    else:
                        cur.execute("SELECT start_interval FROM Slots "
                                    "WHERE start_interval == (?) AND booking_id NOT null", [interval])
                else:
                    cur.execute("SELECT start_interval FROM Slots WHERE start_interval == (?)", [interval])
            interval += timedelta(minutes=15)

            for results in cur:
                for result in results:
                    lst.append(convert_from_utc(result))
        collapse_intervals(lst)

    if params.day:
        params_start = convert_to_utc_day(params.day)
        params_end = params_start + timedelta(days=1)
        interval = params_start
        while interval < params_end:
            with db.create_connection(params.path) as con:
                cur = con.cursor()

                if params.filter:
                    if params.filter == "free":
                        cur.execute("SELECT start_interval FROM Slots "
                                    "WHERE start_interval == (?) AND booking_id is null", [interval])
                    else:
                        cur.execute("SELECT start_interval FROM Slots "
                                    "WHERE start_interval == (?) AND booking_id NOT null", [interval])
                else:
                    cur.execute("SELECT start_interval FROM Slots WHERE start_interval == (?)", [interval])
            interval += timedelta(minutes=15)

            for results in cur:
                for result in results:
                    lst.append(convert_from_utc(result))
        collapse_intervals(lst)
