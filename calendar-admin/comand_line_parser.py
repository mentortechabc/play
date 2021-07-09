import argparse
import get_slots as gs
import delete_day as dd
import delete_interval as di
import add_interval as ai
import re
import db


def createParser():
    """создает парсер,подпарсер с аргументами командной строки"""
    parser = argparse.ArgumentParser(
        description="reads commands and arguments")
    parser.add_argument('--path', '-p', default=':memory:')
    subparsers = parser.add_subparsers(dest='command')

    add_interval = subparsers.add_parser('add_interval')
    add_interval.add_argument('start', help="start date YYYY-MM-DD:HH:MM")
    add_interval.add_argument('end', help="end date YYYY-MM-DD:HH:MM")

    delete_interval = subparsers.add_parser('delete_interval')
    delete_interval.add_argument('start', help="start date YYYY-MM-DD:HH:MM")
    delete_interval.add_argument('end', help="end date YYYY-MM-DD:HH:MM")

    delete_day = subparsers.add_parser('delete_day')
    delete_day.add_argument('date', help="date YYYY-MM-DD")

    get_slots = subparsers.add_parser('get_slots')
    get_slots.add_argument('--week', '-w', help="7 days from date YYYY-MM-DD")
    get_slots.add_argument('--day', '-d', help="day YYYY-MM-DD")
    get_slots.add_argument(
        '--filter', '-f', help="booking or free", choices=['booking', 'free'])

    return parser


def check_func():
    """проверяет на правильность команд"""

    parser = createParser()
    params = parser.parse_args()
    con = db.create_connection(params.path)
    db.create_slots_table(con)
    db.create_admininfo_table(con)
    db.create_bookinginfo_table(con)

    if params.command == "add_interval":
        check_format_add_interval(params, ai.add_interval)
    elif params.command == "delete_interval":
        check_format_add_interval(params, di.delete_interval)
    elif params.command == "delete_day":
        check_format_delete_day(params)
    elif params.command == "get_slots":
        check_format_get_slots(params)
    else:
        print("Wrong command!")


def check_format_add_interval(params, func):
    """запуск функции add_interval и delete_interval если аргументы соответствуют условию"""
    if (regular_start_end(params.start) is True) and (regular_start_end(params.end) is True):
        func(params)
    else:
        print("wrong format add_interval")


def check_format_delete_day(params):
    """запуск функции delete_day, если аргументы соответствуют условию"""
    if regular_day(params.date) is True:
        dd.delete_day(params)
    else:
        print("wrong format delete_day")


def check_format_get_slots(params):
    """запуск функции get_slots, если аргументы соответствуют условию"""
    if (check_day_week(params.week) is False) or (check_day_week(params.day) is False) or (check_filter(params) is False):
        print("wrong format get_slots")
    else:
        gs.get_slots(params)


def check_day_week(params):
    """проверка что day не равен None"""
    if params is not None:
        return regular_day(params)
    else:
        return True


def check_filter(params):
    """проверка что filter не равен None"""
    if params.filter is not None:
        return regular_filter(params.filter)
    else:
        return True


def regular_filter(x):
    """проверка соответствия filter одному из двух значений[booking,free]"""
    if (x == "booking") or (x == "free"):
        return True
    else:
        return False


def regular_start_end(x):
    """регулярка для проверки формата start и end[YYYY-MM-DD:HH:MM]"""
    pattern = r'^([0-9]{4}[-]?((0[13-9]|1[012])[-]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-]?31|02[-]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048])00)[-]?02[-]?29)[:](0[0-1]|1[0-9]|2[0-3])[:]([0-5]{1}[0-9]{1})$'
    if re.match(pattern, x):
        return True
    else:
        return False


def regular_day(x):
    """регулярка для проверки формата date[YYYY-MM-DD]"""
    pattern = r'^([0-9]{4}[-]?((0[13-9]|1[012])[-]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-]?31|02[-]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048])00)[-]?02[-]?29)$'
    if re.match(pattern, x):
        return True
    else:
        return False
