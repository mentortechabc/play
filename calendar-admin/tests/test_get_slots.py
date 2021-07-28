from types import SimpleNamespace
import get_slots
from .func_for_test_db import clean_table_slots, create_test_table
import add_interval
import pytest


@pytest.fixture(scope='module')
def create_test_table_with_data_for_get_slots():
    params_for_add = SimpleNamespace(path="test_main_db.sqlite",
                                     start="2021-03-02T00:00", end="2021-03-10T23:15")
    clean_table_slots(params_for_add)
    create_test_table(params_for_add)
    add_interval.add_interval(params_for_add)


def test_get_slots_week(create_test_table_with_data_for_get_slots):
    params_for_get = SimpleNamespace(path="test_main_db.sqlite",
                                     week="2021-03-02", filter=None, day=None)
    result = get_slots.get_slots(params_for_get)
    assert result == '2021-03-02 00:00:00 - 2021-03-09 00:15:00'


def test_get_slots_day(create_test_table_with_data_for_get_slots):
    params_for_get = SimpleNamespace(path="test_main_db.sqlite",
                                     week=None, filter=None, day="2021-03-02")
    result = get_slots.get_slots(params_for_get)
    assert result == '2021-03-02 00:00:00 - 2021-03-03 00:15:00'
