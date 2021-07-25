from datetime import datetime, timedelta, timezone


def local_to_utc(local_dt):
    """конвертирует время из таймзоны пользователя в UTC0"""
    local_dt = datetime.fromisoformat(local_dt)
    utc_dt = local_dt.astimezone(timezone.utc)
    return utc_dt.replace(tzinfo=None)


def utc_to_local(utc_dt):
    """конвертирует время из UTC0 в соответствии с таймзоной пользователя"""
    utc_dt = datetime.fromisoformat(utc_dt)
    local_dt = utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
    return local_dt.replace(tzinfo=None)


def utc_to_local_format(utc_dt):
    return utc_to_local(utc_dt).isoformat(timespec='minutes')


# print(utc_to_local('2020-06-24T10:15'))


def collapse_intervals(lst):
    """Схлопывает интервалы из списка и выводит пользователю в отфоматированном виде"""
    lst.sort()
    i = -1
    new_lst = []
    while i < len(lst) - 1:
        if lst[i] - timedelta(minutes=15) != lst[i - 1]:
            new_lst.append(lst[i])
        elif lst[i] + timedelta(minutes=15) != lst[i + 1]:
            finish_interval = lst[i] + timedelta(minutes=15)
            new_lst.append(finish_interval)
        i += 1
    new_lst.sort()

    n = 0
    while n < len(new_lst) - 1:
        collapse_interval = ("""{} - {}""".format(new_lst[n], new_lst[n + 1]))
        yield collapse_interval
        n += 2
