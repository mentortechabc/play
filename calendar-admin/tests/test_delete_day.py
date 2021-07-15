from types import SimpleNamespace
import delete_day as dd
from .func_for_test_db import *
import add_interval as ai


def test_delete_day():
    params_for_add = SimpleNamespace(
        path="test_main_db.sqlite", start="2021-03-02:12:00", end="2021-03-02:13:15")
    params = SimpleNamespace(path="test_main_db.sqlite", date="2021-03-02")
    clean_table_slots(params)
    create_test_table(params)
    ai.add_interval(params_for_add)
    dd.delete_day(params)
    result = get_test_slots(params)
    assert result == []


def test_delete_day_1():
    params_for_add = SimpleNamespace(
        path="test_main_db.sqlite", start="2021-03-02:22:45", end="2021-03-03:03:15")
    params = SimpleNamespace(path="test_main_db.sqlite", date="2021-03-02")
    clean_table_slots(params)
    create_test_table(params)
    ai.add_interval(params_for_add)
    dd.delete_day(params)
    result = get_test_slots(params)
    assert len(result) == 13
    assert result[0] == (6, "2021-03-02 21:00:00", None)
    assert result[6] == (12, "2021-03-02 22:30:00", None)
    assert result[12] == (18, "2021-03-03 00:00:00", None)

