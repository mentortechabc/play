import sqlite3 as sq
from datetime import timedelta, datetime


def add_interval(namespace):
    """Добавление интервала в базу данных"""
    namespace_start = datetime.strptime(namespace.start, "%Y-%m-%d:%H:%M")
    namespace_end = datetime.strptime(namespace.end, "%Y-%m-%d:%H:%M")
    interval = namespace_start
    if namespace_start.minute % 15 == 0 and namespace_end.minute % 15 == 0:
        while interval < namespace_end:
            with sq.connect(':memory:') as con:
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
