"""
https://www.concentricsky.com/articles/detail/pythons-hidden-new
"""

class GimmeFive(object):
    def __new__(cls, *args, **kwargs):
        print("new called")
        return 5

    def __init__(self,x):
        """
        never called:
        > If __new__() does not return an instance of cls, then the new instance’s __init__() method will not be invoked.

        See https://docs.python.org/3/reference/datamodel.html#object.__new__
        """
        print("init called")
        self.x = x

five = GimmeFive()
assert five == 5
assert isinstance(five,int) is True
assert hasattr(five, "x") is False


class Something:
    def __init__(self, param):
        print(f"init something, param={param}")

class ClassWithCustomNew:
    def __new__(cls, *args, **kwargs):
        print("ClassWithCustomNew - new called")
        return object.__new__(Something)

    def __init__(self, x):
        print("ClassWithCustomNew - init")


class ClassWithCustomNew2:
    def __new__(cls, *args, **kwargs):
        print("ClassWithCustomNew2 - new called")
        return Something(*args, **kwargs)

    def __init__(self, x):
        print("ClassWithCustomNew2 - init")



print("--------------------")
x = ClassWithCustomNew(123)
print(x)
assert isinstance(x, Something)


x = ClassWithCustomNew2(123)
print(x)
assert isinstance(x, Something)
