from types import SimpleNamespace
import add_interval as ai
from .func_for_test_db import *
        

def test_add_interval():
    params = SimpleNamespace(path="test_main_db.sqlite", start="2021-03-02:12:00", end="2021-03-02:13:15")
    clean_table_slots(params)
    create_test_table(params)
    ai.add_interval(params)
    result = get_test_slots(params)
    assert len(result) == 5
    assert result[0] == (1, "2021-03-02 09:00:00", None)
    assert result[1] == (2, "2021-03-02 09:15:00", None)
    


# нужен return из else
# def test_add_interval_negative():
#     params = SimpleNamespace(path="test_main_db.sqlite", start="2021-03-02:12:10", end="2021-03-02:13:15")
#     assert ai.add_interval(params) == "Введите интервал кратный 15 минутам"
