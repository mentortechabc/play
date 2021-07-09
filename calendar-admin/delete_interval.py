import sqlite3 as sq
from datetime import timedelta, datetime


def delete_interval(namespace):
    """удаляем интервал"""
    namespace_start = datetime.strptime(namespace.start, "%Y-%m-%d:%H:%M")
    namespace_end = datetime.strptime(namespace.end, "%Y-%m-%d:%H:%M")
    interval = namespace_start
    if namespace_start.minute % 15 == 0 and namespace_end.minute % 15 == 0:
        while interval < namespace_end:
            with sq.connect(namespace.path) as con:
                cur = con.cursor()

                cur.execute("DELETE FROM slot WHERE start_interval == (?)", [interval])
            interval += timedelta(minutes=15)
    else:
        print('Введите интервал кратный 15 минутам')
