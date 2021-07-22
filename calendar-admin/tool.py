#!/Usr/bin/env python
import argparse
import db
from convert_time import convert_from_utc, convert_to_utc_day, collapse_and_print_intervals
from datetime import timedelta


def createParser():
    """создает парсер,подпарсер с аргументами командной строки"""
    parser = argparse.ArgumentParser(
        description="reads commands and arguments",
        prog="test tool")
    parser.add_argument('--path', '-p', default='main_db.sqlite',
                        help="the path to the database. Default: main_db.sqlite")
    subparsers = parser.add_subparsers(dest='command',
                                       title="Used commands",
                                       description='Commands to be taken as the first parameter %(prog)s')

    add_interval = subparsers.add_parser('booking')
    add_interval.add_argument(
        'start', help="start of added interval: YYYY-MM-DDThh:mm")
    add_interval.add_argument(
        'end', help="end of added interval: YYYY-MM-DDThh:mm")
    add_interval.add_argument('name', help="name: <First name>")
    add_interval.add_argument('email', help="email")
    add_interval.add_argument('-t', '--topic', help="messsage")

    add_interval = subparsers.add_parser('get')
    add_interval.add_argument(
        'day', help="start of added interval: YYYY-MM-DD")
    add_interval.add_argument('--filter', default="free")
    return parser


def get_intervals_from_db(params, params_start, params_end):
    """получает объект со слотами из базы данных в зависимости от фильтра"""
    with db.create_connection(params.path) as con:
        cur = con.cursor()
        SELECT_QUERY = "SELECT start_interval FROM Slots WHERE (?) <= start_interval AND (?) >= start_interval AND booking_id is null"
        cur.execute(SELECT_QUERY, [params_start, params_end])
        return cur


def get_slots(params):
    """выводит отформатированный список слотов за неделю или за день"""
    lst_of_intervals = []

    if params.day:
        param_start = convert_to_utc_day(params.day)
        param_end = param_start + timedelta(days=1)

        intervals = get_intervals_from_db(params, param_start, param_end)
        for interval_tuple in intervals:
            assert len(interval_tuple) == 1
            interval = interval_tuple[0]
            lst_of_intervals.append(convert_from_utc(interval))
        collapse_interval = collapse_and_print_intervals(lst_of_intervals)
        print(collapse_interval)
        return collapse_interval


def correctness_commands(params):
    """проверяет на правильность команд"""

    if params.command == "get":
        get_slots(params)
    elif params.command == "booking":
        booking(params)


def booking(params):
    with db.create_connection(params.path) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO BookingInfo VALUES (NULL,?,?,?)",
                    (params.name, params.email, params.topic))


parser = createParser()
params = parser.parse_args()
correctness_commands(params)
