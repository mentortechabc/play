import comand_line_parser as comlipa
import pytest


@pytest.mark.parametrize("filter", [("free"),
                                    ("booking")])
def test_regular_filter_true(filter):
    assert comlipa.regular_filter(filter) is True


@pytest.mark.parametrize("filter", [("123"),
                                    ("bear"),
                                    ("!@#$%^&*()_+?><,./")])
def test_regular_filter_false(filter):
    assert comlipa.regular_filter(filter) is False
