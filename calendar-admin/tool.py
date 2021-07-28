#!/Usr/bin/env python
import argparse
import db
from convert_time import local_to_utc
from datetime import timedelta


def createParser():
    """создает парсер,подпарсер с аргументами командной строки"""
    parser = argparse.ArgumentParser(
        description="reads commands and arguments",
        prog="test tool")
    parser.add_argument('--path', '-p', default='main_db.sqlite',
                        help="the path to the database. Default: main_db.sqlite")
    parser.add_argument(
        'start', help="start of added interval: YYYY-MM-DDThh:mm")
    parser.add_argument(
        'end', help="end of added interval: YYYY-MM-DDThh:mm")
    parser.add_argument('name', help="name: <First name>")
    parser.add_argument('email', help="email")
    parser.add_argument('-t', '--topic', help="messsage")

    return parser


def booking(params):
    with db.create_connection(params.path) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO BookingInfo VALUES (NULL,?,?,?)",
                    (params.name, params.email, params.topic))
        cur.execute("SELECT MAX(id) AS Last FROM BookingInfo")
        booking_id = cur.fetchall()
        for x in booking_id:
            res = x[0]
        params_start = local_to_utc(params.start)
        params_end = local_to_utc(params.end)
        while params_start < params_end:
            cur.execute(
                "UPDATE Slots SET booking_id = (?) WHERE start_interval = (?)", (res, params_start))
            params_start += timedelta(minutes=15)


parser = createParser()
params = parser.parse_args()
booking(params)
