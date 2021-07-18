from types import SimpleNamespace
import add_interval
from .func_for_test_db import clean_table_slots, create_test_table, get_test_slots, convert_from_utc_test


def test_add_interval():
    params = SimpleNamespace(path="test_main_db.sqlite",
                             start="2021-03-02T12:00", end="2021-03-02T13:15")
    clean_table_slots(params)
    create_test_table(params)
    add_interval.add_interval(params)
    result = get_test_slots(params)
    lst = convert_from_utc_test(result)
    assert len(lst) == 5
    assert lst[0] == '2021-03-02:12:00'
    assert lst[1] == '2021-03-02:12:15'


def test_add_interval_negative():
    params = SimpleNamespace(path="test_main_db.sqlite", start="2021-03-02T12:10", end="2021-03-02T13:15")
    assert add_interval.add_interval(params) == "Введите интервал кратный 15 минутам"
