import argparse


def createParser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    add_interval = subparsers.add_parser('add_interval')
    add_interval.add_argument('start')
    add_interval.add_argument('end')

    delete_interval = subparsers.add_parser('delete_interval')
    delete_interval.add_argument('start')
    delete_interval.add_argument('end')

    delete_day = subparsers.add_parser('delete_day')
    delete_day.add_argument('date')

    get_slots = subparsers.add_parser('get_slots')
    get_slots.add_argument('--week', '-w')
    get_slots.add_argument('--day', '-d')
    get_slots.add_argument('--filter', '-f')

    return parser


def add_interval(namespace):
    """добавление интервала"""
    print("добавляем, интервал  от {} до {}".format(
        namespace.start, namespace.end))


def delete_interval(namespace):
    """удаляем интервал"""
    print("удаляем, интервал  от {} до {}".format(
        namespace.start, namespace.end))


def delete_day(namespace):
    """удаляем день"""
    print("удаляем {} день".format(namespace.date))


def get_slots(namespace):
    """получаем список слотов"""
    if namespace.week:
        print("слоты недели: {}".format(namespace.week))
    if namespace.day:
        print("слоты дня: {}".format(namespace.day))
    if namespace.filter:
        print("фильтр: {}".format(namespace.filter))


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    if namespace.command == "add_interval":
        add_interval(namespace)
    elif namespace.command == "delete_interval":
        delete_interval(namespace)
    elif namespace.command == "delete_day":
        delete_day(namespace)
    elif namespace.command == "get_slots":
        get_slots(namespace)
    else:
        print("Что-то пошло не так...")
