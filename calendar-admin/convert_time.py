from datetime import datetime, timedelta


def convert_to_utc(params_time):
    """конвертирует время из таймзоны пользователя в UTC0"""
    params_time = datetime.strptime(params_time, "%Y-%m-%dT%H:%M")
    timezone = datetime.now()-datetime.utcnow()
    params_time -= timezone
    return params_time


def convert_to_utc_day(params_time):
    """конвертирует дату из таймзоны пользователя в UTC0"""
    params_time = datetime.strptime(params_time, "%Y-%m-%d")
    timezone = datetime.now()-datetime.utcnow()
    params_time -= timezone
    return params_time


def convert_from_utc(params_time):
    """конвертирует время из UTC0 в соответствии с таймзоной пользователя"""
    timezone = datetime.now()-datetime.utcnow()
    params_time = datetime.strptime(params_time, "%Y-%m-%d %H:%M:%S")
    params_time += timezone
    return params_time


def collapse_and_print_intervals(lst):
    """Схлопывает интервалы из списка и выводит пользователю в отфоматированном виде"""
    i = -1
    new_lst = []
    while i < len(lst) - 1:
        if lst[i] + timedelta(minutes=15) != lst[i + 1] or lst[i] - timedelta(minutes=15) != lst[i - 1]:
            new_lst.append(lst[i])
        i += 1
    new_lst.sort()

    n = 0
    while n < len(new_lst) - 1:
        collapse_interval = ("""{} - {}""".format(new_lst[n], new_lst[n + 1]))
        return collapse_interval
    n += 2
