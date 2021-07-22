import db
from convert_time import convert_to_utc, convert_from_utc
from datetime import timedelta


def add_interval(params):
    """Добавление интервала в базу данных"""
    params_start = convert_to_utc(params.start)
    params_end = convert_to_utc(params.end)
    if params_start.minute % 15 == 0 and params_end.minute % 15 == 0:
        while params_start < params_end:
            with db.create_connection(params.path) as con:
                cur = con.cursor()

                cur.execute("SELECT start_interval FROM Slots WHERE start_interval == (?)", [params_start])
                interval_list = cur.fetchall()
                if len(interval_list) > 0:
                    assert len(interval_list) == 1
                    interval_tuple = interval_list[0]
                    assert len(interval_tuple) == 1
                    interval = interval_tuple[0]

                    print('interval {} - {} already exist'.format(convert_from_utc(interval),
                                                                  convert_from_utc(interval)+timedelta(minutes=15)))
                else:
                    cur.execute("INSERT INTO Slots (start_interval) VALUES (?)", [params_start])
            params_start += timedelta(minutes=15)
    else:
        mes = 'Введите интервал кратный 15 минутам'
        print(mes)
        return mes
