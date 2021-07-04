
def get_slots(namespace):
    """получаем список слотов"""
    if namespace.week:
        print("week slots: {}".format(namespace.week))
    if namespace.day:
        print("day slots: {}".format(namespace.day))
    if namespace.filter:
        print("filter: {}".format(namespace.filter))
