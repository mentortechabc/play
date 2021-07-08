import libr


def f(lst, x, mult=2):
    lst.append(x * mult)


# pytest
def test_f():
    lst = [1, 2, 3]
    f(lst, 4)
    assert lst == [1, 2, 3, 8]


if __name__ == '__main__':
    libr.hello()
    print("john")
