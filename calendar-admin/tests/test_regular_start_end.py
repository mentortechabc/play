import comand_line_parser as comlipa
import pytest


@pytest.mark.parametrize("date", [("2021-01-02:11:00"),
                                  ("2020-10-15:09:15")])
def test_regular_start_end_positive(date):
    assert comlipa.regular_start_end(date) is True


@pytest.mark.parametrize("date", [("2021-13-02:11:00"),
                                  ("2021-01-32:11:00"),
                                  ("2021-01-02:25:00"),
                                  ("2021-01-02:11:60"),
                                  ("2021-01-02:11:0"),
                                  ("2021-02-30:11:00")])
def test_regular_start_end_negative(date):
    assert comlipa.regular_start_end(date) is False
