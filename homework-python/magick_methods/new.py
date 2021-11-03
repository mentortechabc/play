"""
https://howto.lintel.in/python-__new__-magic-method-explained/

"""


class Singleton(object):
    _instance = None  # Keep instance reference

    def __new__(cls, *args, **kwargs):
        print(f"running __new__ with cls = {cls}")
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, x):
        print(f"running Singleton init, x = {x}")
        # this doesn't make sense for singleton. Just for learning purposes
        self.x = x


if __name__ == '__main__':
    a = Singleton(1)
    b = Singleton(2)
    print(a, a.x)
    print(b, b.x)
