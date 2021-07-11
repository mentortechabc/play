import db
from convert_time import convert_from_utc, convert_to_utc_day, collapse_intervals
from datetime import timedelta


def get_intervals_from_db(params_path, params_filter, params_start, params_end):
    """получает объект со слотами из базы данных в зависимости от фильтра"""
    with db.create_connection(params_path) as con:
        cur = con.cursor()

        SELECT_QUERY = "SELECT start_interval FROM Slots WHERE (?) <= start_interval <= (?) "

        if params_filter:
            if params_filter == "free":
                SELECT_QUERY += "AND booking_id is null"
                cur.execute(SELECT_QUERY, [params_start, params_end])
            else:
                SELECT_QUERY += "AND booking_id NOT null"
                cur.execute(SELECT_QUERY, [params_start, params_end])
        else:
            cur.execute(SELECT_QUERY, [params_start, params_end])
        return cur


def get_slots(params):
    """выводит отформатированный список слотов за неделю или за день"""
    lst_of_intervals = []
    if params.week:
        param_start = convert_to_utc_day(params.week)
        param_end = param_start + timedelta(days=7)

        intervals = get_intervals_from_db(params.path, params.filter, param_start, param_end)
        for interval_tuple in intervals:
            assert len(interval_tuple) == 1
            interval = interval_tuple[0]
            lst_of_intervals.append(convert_from_utc(interval))
        collapse_intervals(lst_of_intervals)

    if params.day:
        param_start = convert_to_utc_day(params.day)
        param_end = param_start + timedelta(days=1)

        intervals = get_intervals_from_db(params.path, params.filter, param_start, param_end)
        for interval_tuple in intervals:
            assert len(interval_tuple) == 1
            interval = interval_tuple[0]
            lst_of_intervals.append(convert_from_utc(interval))
        collapse_intervals(lst_of_intervals)
