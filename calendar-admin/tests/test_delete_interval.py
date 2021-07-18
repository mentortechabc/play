from types import SimpleNamespace
import delete_interval
from .func_for_test_db import clean_table_slots, create_test_table, get_test_slots, convert_from_utc_test
import add_interval as ai


def test_delete_interval():
    params_for_add = SimpleNamespace(
        path="test_main_db.sqlite", start="2021-03-02T12:00", end="2021-03-02T13:15")
    params_for_del = SimpleNamespace(
        path="test_main_db.sqlite", start="2021-03-02T12:00", end="2021-03-02T12:45")
    clean_table_slots(params_for_del)
    create_test_table(params_for_del)
    ai.add_interval(params_for_add)
    delete_interval.delete_interval(params_for_del)
    result = get_test_slots(params_for_del)
    lst = convert_from_utc_test(result)
    assert len(lst) == 1
    assert lst[0] == "2021-03-02:13:00"


def test_delete_interval_1():
    params = SimpleNamespace(
        path="test_main_db.sqlite", start="2021-03-02T12:00", end="2021-03-02T13:15")
    clean_table_slots(params)
    create_test_table(params)
    ai.add_interval(params)
    delete_interval.delete_interval(params)
    result = get_test_slots(params)
    lst = convert_from_utc_test(result)
    assert len(lst) == 0
    assert lst == []
