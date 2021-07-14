import comand_line_parser as comlipa



def test_regular_filter_positive():

    assert comlipa.regular_filter("free") is True
    assert comlipa.regular_filter("booking") is True


def test_regular_filter_negative():
    assert comlipa.regular_filter("132") is False
    assert comlipa.regular_filter("bear") is False
    assert comlipa.regular_filter("!@#$%^&*()_+?><,./") is False
