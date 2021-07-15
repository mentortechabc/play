from types import SimpleNamespace
import delete_interval as di
from .func_for_test_db import *
import add_interval as ai


def test_delete_interval():
    params_for_add = SimpleNamespace(
        path="test_main_db.sqlite", start="2021-03-02:12:00", end="2021-03-02:13:15")
    params_for_del = SimpleNamespace(
        path="test_main_db.sqlite", start="2021-03-02:12:00", end="2021-03-02:12:45")
    clean_table_slots(params_for_del)
    create_test_table(params_for_del)
    ai.add_interval(params_for_add)
    di.delete_interval(params_for_del)
    result = get_test_slots(params_for_del)
    assert len(result)==2
    assert result[0] == (4, "2021-03-02 09:45:00", None)
    assert result[1] == (5, "2021-03-02 10:00:00", None)


def test_delete_interval_1():
    params = SimpleNamespace(
        path="test_main_db.sqlite", start="2021-03-02:12:00", end="2021-03-02:13:15")
    clean_table_slots(params)
    create_test_table(params)
    ai.add_interval(params)
    di.delete_interval(params)
    result = get_test_slots(params)
    assert len(result)==0
    assert result == []
