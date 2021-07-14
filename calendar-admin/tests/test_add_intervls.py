import pytest
from types import SimpleNamespace
import db
import add_interval as ai

@pytest.mark.parametrize("path, start, end", [("test_main_db.sqlite", '2021-03-02:12:00', '2021-03-02:13:15')])
def test_add_interval(path, start, end):
    params = SimpleNamespace(path=path, start=start, end=end)

    #нужно пофиксить :memory:, тогда можноубрать создание
    con = db.create_connection(params.path)
    db.create_slots_table(con)
    db.create_admininfo_table(con)
    db.create_bookinginfo_table(con)

    ai.add_interval(params)
    with db.create_connection(params.path) as con:
        cur = con.cursor()
        a = cur.execute(
            "SELECT * FROM Slots")
        result = a.fetchall()
        assert len(result) == 5
        assert result[0] == (1,'2021-03-02 09:00:00', None) 
        assert result[1] == (2,'2021-03-02 09:15:00', None) 



# нужен return из else
# @pytest.mark.parametrize("path, start, end", [("test_main_db.sqlite", '2021-03-02:12:10', '2021-03-02:13:15')])
# def test_add_interval_negative(path, start, end):
#     params = SimpleNamespace(path=path, start=start, end=end)

#     con = db.create_connection(params.path)
#     db.create_slots_table(con)
#     db.create_admininfo_table(con)
#     db.create_bookinginfo_table(con)
#     assert ai.add_interval(params) == 'Введите интервал кратный 15 минутам'
    