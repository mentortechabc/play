from types import SimpleNamespace
import delete_day
from .func_for_test_db import clean_table_slots, create_test_table, get_test_slots, convert_from_utc_test
import add_interval


def test_delete_day():
    params_for_add = SimpleNamespace(
        path="test_main_db.sqlite", start="2021-03-02T12:00", end="2021-03-02T13:15")
    params = SimpleNamespace(path="test_main_db.sqlite", date="2021-03-02")
    clean_table_slots(params)
    create_test_table(params)
    add_interval.add_interval(params_for_add)
    delete_day.delete_day(params)
    result = get_test_slots(params)
    lst = convert_from_utc_test(result)
    assert lst == []


def test_delete_day_1():
    params_for_add = SimpleNamespace(
        path="test_main_db.sqlite", start="2021-03-02T22:45", end="2021-03-03T03:15")
    params = SimpleNamespace(path="test_main_db.sqlite", date="2021-03-02")
    clean_table_slots(params)
    create_test_table(params)
    add_interval.add_interval(params_for_add)
    delete_day.delete_day(params)
    result = get_test_slots(params)
    lst = convert_from_utc_test(result)
    assert len(lst) == 12
    assert lst[0] == '2021-03-03:00:15'
    assert lst[6] == '2021-03-03:01:45'
    assert lst[11] == '2021-03-03:03:00'
