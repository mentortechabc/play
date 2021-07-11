import db
from convert_time import convert_to_utc_day
from datetime import timedelta


def delete_day(params):
    """удаляет незанятые интервалы дня"""
    params_start = convert_to_utc_day(params.date)
    params_end = params_start + timedelta(days=1)
    interval = params_start
    while interval < params_end:
        with db.create_connection(params.path) as con:
            cur = con.cursor()

            cur.execute("DELETE FROM Slots WHERE start_interval == (?) AND booking_id is null", [interval])
            cur.execute("SELECT start_interval FROM Slots "
                        "WHERE start_interval == (?) AND booking_id != '(None,)'", [interval])
            for result in cur:
                print("""booked interval: {}""".format(result))
        interval += timedelta(minutes=15)
