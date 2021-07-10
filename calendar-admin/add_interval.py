import db
from datetime import timedelta, datetime


def add_interval(params):
    """Добавление интервала в базу данных"""
    params_start: datetime = datetime.strptime(params.start, "%Y-%m-%d:%H:%M")
    params_end = datetime.strptime(params.end, "%Y-%m-%d:%H:%M")
    interval = params_start
    if params_start.minute % 15 == 0 and params_end.minute % 15 == 0:
        while interval < params_end:
            with db.create_connection(params.path) as con:
                cur = con.cursor()

                cur.execute("SELECT start_interval FROM slot WHERE start_interval == (?)", [interval])
                intervals = cur.fetchall()
                if len(intervals) > 0:
                    print('interval {} already exist'.format(interval))
                else:
                    cur.execute("INSERT INTO slot (start_interval) VALUES (?)", [interval])
            interval += timedelta(minutes=15)
    else:
        print('Введите интервал кратный 15 минутам')
