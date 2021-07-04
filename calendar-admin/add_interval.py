import sqlite3 as sq
from datetime import timedelta, datetime


# def add_interval(namespace):
#     """добавление интервала"""
#     print("add interval {} to {}".format(
#         namespace.start, namespace.end))
def add_interval(namespace_start, namespace_end):
    interval = namespace_start
    if namespace_start.minute % 15 == 0 and namespace_end.minute % 15 == 0:
        while interval < namespace_end:
            with sq.connect('database.db') as con:
                cur = con.cursor() #Cursor

                cur.execute("INSERT INTO slot (start) VALUES (?)", [interval])
            print(interval)
            interval += timedelta(minutes=15)
    else:
        print('Введите интервал кратный 15 минутам')


date_a = datetime(2020, 6, 24, 10, 30)
date_b = datetime(2020, 6, 24, 20, 30)
if date_a.minute % 15 == 0:
    print('rigth time')
add_interval(date_a, date_b)
