def f():
    s = 0
    for i in range(1000):
        s += i ** 2
    return s


g = f


def h():
    return 10


f = h

# def f():
#     return 10


print("f", f())
print("g", g())

exit()


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def apply(value, fn):
    return fn(value)


def outer(x):
    def pow(value):
        return value ** x

    return pow


# pow3 = outer(3)
# pow2 = outer(2)
# print(pow3(10))
# print(pow2(10))

# some library start
def square(x: int) -> int:
    return x ** 2


def cube(x):
    return x ** 3


# some library end

import time


def decorate(fn):
    def wrapped(x):
        start = time.time_ns()
        res = fn(x)
        end = time.time_ns()
        print("The function call tool {}".format(end - start))
        return res

    return wrapped


decorated_square = decorate(square)
decorated_cube = decorate(cube)


@decorate
def another_square(x):
    return x ** 2 + 1


print(decorated_square)
result = decorated_square(10)
print("result ", result)

result = decorated_cube(10)
print("result ", result)

result = another_square(10)
print("result another_square", result)

# print("f(): ", f())
# print("g(): ", g())
# print("f: ", f)
# print("g: ", g)


# семантика присваивания ???
