from types import SimpleNamespace
import get_slots
from .func_for_test_db import clean_table_slots, create_test_table, get_test_slots, convert_from_utc_test
import add_interval


def test_get_slots_week():
    params_for_add = SimpleNamespace(path="test_main_db.sqlite",
                                     start="2021-03-02T00:00", end="2021-03-10T23:15")
    params_for_get = SimpleNamespace(path="test_main_db.sqlite",
                                     week="2021-03-02", filter=None, day=None)
    clean_table_slots(params_for_add)
    create_test_table(params_for_add)
    add_interval.add_interval(params_for_add)
    result = get_slots.get_slots(params_for_get)
    assert result == '2021-03-02 00:00:00 - 2021-03-09 00:00:00'

#нужен tool который будет менять free на booking
# def test_get_slots_week_with_filter_free():
#     params_for_add = SimpleNamespace(path="test_main_db.sqlite",
#                                      start="2021-03-02:00:00", end="2021-03-10:23:15")
#     params_for_get = SimpleNamespace(path="test_main_db.sqlite",
#                                      week="2021-03-02", filter="free", day=None)
#     clean_table_slots(params_for_add)
#     create_test_table(params_for_add)
#     add_interval.add_interval(params_for_add)
#     result = get_slots.get_slots(params_for_get)
#     assert result == '2021-03-02 00:00:00 - 2021-03-09 00:00:00'


# def test_get_slots_week_with_filter_booking():
#     params_for_add = SimpleNamespace(path="test_main_db.sqlite",
#                                      start="2021-03-02:00:00", end="2021-03-10:23:15")
#     params_for_get = SimpleNamespace(path="test_main_db.sqlite",
#                                      week="2021-03-02", filter="booking", day=None)
#     clean_table_slots(params_for_add)
#     create_test_table(params_for_add)
#     add_interval.add_interval(params_for_add)
#     result = get_slots.get_slots(params_for_get)
#     assert result == '2021-03-02 00:00:00 - 2021-03-09 00:00:00'


def test_get_slots_day():
    params_for_add = SimpleNamespace(path="test_main_db.sqlite",
                                     start="2021-03-02T00:00", end="2021-03-04T23:15")
    params_for_get = SimpleNamespace(path="test_main_db.sqlite",
                                     week=None, filter=None, day="2021-03-02")
    clean_table_slots(params_for_add)
    create_test_table(params_for_add)
    add_interval.add_interval(params_for_add)
    result = get_slots.get_slots(params_for_get)
    assert result == '2021-03-02 00:00:00 - 2021-03-03 00:00:00'


# def test_get_slots_day_with_filter_free():
#     params_for_add = SimpleNamespace(path="test_main_db.sqlite",
#                                      start="2021-03-02:00:00", end="2021-03-04:23:15")
#     params_for_get = SimpleNamespace(path="test_main_db.sqlite",
#                                      week=None, filter='free', day="2021-03-02")
#     clean_table_slots(params_for_add)
#     create_test_table(params_for_add)
#     add_interval.add_interval(params_for_add)
#     result = get_slots.get_slots(params_for_get)
#     assert result == '2021-03-02 00:00:00 - 2021-03-03 00:00:00'


# def test_get_slots_day_with_filter_booking():
#     params_for_add = SimpleNamespace(path="test_main_db.sqlite",
#                                      start="2021-03-02:00:00", end="2021-03-04:23:15")
#     params_for_get = SimpleNamespace(path="test_main_db.sqlite",
#                                      week=None, filter='booking', day="2021-03-02")
#     clean_table_slots(params_for_add)
#     create_test_table(params_for_add)
#     add_interval.add_interval(params_for_add)
#     result = get_slots.get_slots(params_for_get)
#     assert result == '2021-03-02 00:00:00 - 2021-03-03 00:00:00'
