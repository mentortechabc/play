import db
from convert_time import convert_to_utc
from datetime import timedelta, datetime


def delete_interval(params):
    """удаляем интервал"""
    params_start = convert_to_utc(params.start)
    params_end = convert_to_utc(params.end)
    interval = params_start
    if params_start.minute % 15 == 0 and params_end.minute % 15 == 0:
        while interval < params_end:
            with db.create_connection(params.path) as con:
                cur = con.cursor()

                cur.execute("DELETE FROM slot WHERE start_interval == (?)", [interval])
            interval += timedelta(minutes=15)
    else:
        print('Введите интервал кратный 15 минутам')
