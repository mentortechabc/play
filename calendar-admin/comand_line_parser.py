import argparse
import get_slots as gs
import delete_day as dd
import delete_interval as di
import add_interval as ai
import re


def createParser():
    """создает парсер,подпарсер с аргументами командной строки"""
    parser = argparse.ArgumentParser(
        description="reads commands and arguments")
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
    get_slots.add_argument('--week', '-w', help="#######")
    get_slots.add_argument('--day', '-d', help="day YYYY-MM-DD")
    get_slots.add_argument(
        '--filter', '-f', help="booking or free", choices=['booking', 'free'])

    return parser


def check_func():
    """проверяет на правильность команд"""

    parser = createParser()
    namespace = parser.parse_args()

    if namespace.command == "add_interval":
        check_format_add_interval(namespace, ai.add_interval)
    elif namespace.command == "delete_interval":
        check_format_add_interval(namespace, di.delete_interval)
    elif namespace.command == "delete_day":
        chech_format_delete_day(namespace)
    elif namespace.command == "get_slots":
        check_format_get_slots(namespace)
    else:
        print("Ups...")


def check_format_add_interval(namespace, func):
    """запуск функции add_interval и delete_interval если аргументы соответствуют условию"""
    if (regular_start_end(namespace.start) is True) and (regular_start_end(namespace.end) is True):
        func(namespace)
    else:
        print("wrong format add_interval")

# def check_format_add_interval(namespace):
#     """запуск функции add_interval, если аргументы соответствуют условию"""
#     if (regular_start_end(namespace.start) is True) and (regular_start_end(namespace.end) is True):
#         ai.add_interval(namespace)
#     else:
#         print("wrong format add_interval")


# def check_format_delete_interval(namespace):
#     """запуск функции delete_interval если аргументы соответствуют условию"""
#     if (regular_start_end(namespace.start) is True) and (regular_start_end(namespace.end) is True):
#         di.delete_interval(namespace)
#     else:
#         print("wrong format delete_interval")


def chech_format_delete_day(namespace):
    """запуск функции delete_day, если аргументы соответствуют условию"""
    if regular_day(namespace.date) is True:
        dd.delete_day(namespace)
    else:
        print("wrong format delete_day")


def check_format_get_slots(namespace):
    """запуск функции get_slots, если аргументы соответствуют условию"""
    if (check_week(namespace) is False) or (check_day(namespace) is False) or (check_filter(namespace) is False):
        print("wrong format get_slots")
    else:
        gs.get_slots(namespace)


def check_week(namespace):
    """проверяет что week не равен None"""
    if namespace.week is not None:
        return regular_week(namespace.week)
    else:
        return True


def regular_week(namespace):
    """регулярка для проверки формата week"""
    return True
# уточнить формат недели и сделать регулярку


def check_day(namespace):
    """проверка что day не равен None"""
    if namespace.day is not None:
        return regular_day(namespace.day)
    else:
        return True


def check_filter(namespace):
    """проверка что filter не равен None"""
    if namespace.filter is not None:
        return regular_filter(namespace.filter)
    else:
        return True


def regular_filter(x):
    """проверка соответствия filter одному из двух значений[booking,free]"""
    if (x == "booking") or (x == "free"):
        return True
    else:
        return False


def regular_start_end(x):
    """решулярка для проверки формата start и end[YYYY-MM-DD:HH:MM]"""
    pattern = r'[0-9]{4}[-][0-9]{2}[-][0-9]{2}[:][0-9]{2}[:][0-9]{2}$'
    if re.match(pattern, x):
        return True
    else:
        return False


def regular_day(x):
    """регулярка для проверки формата date[YYYY-MM-DD]"""
    pattern = r'[0-9]{4}[-][0-9]{2}[-][0-9]{2}$'
    if re.match(pattern, x):
        return True
    else:
        return False
