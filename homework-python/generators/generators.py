lst = [1, 2, 3]

for x in lst:
    print(x)

r = range(3)
print(r)
print(type(r))

for x in r:
    print(x)

squares = (x ** 2 for x in range(10))
print(squares)

for x in squares:
    print(x, end=' ')

squares_list = tuple(squares)
print(squares_list)

squares_list = tuple(squares)
print(squares_list)

print("another way")


def create_generator():
    for i in range(10):
        yield i ** 2  # <----


squares_gen = create_generator()
print(squares_gen)

for x in squares_gen:
    print(x, end=" ")
print()

print(list(squares_gen))

print(list(squares_gen))

print("using generators in context managers")

#
# n = 10
# f = open("file.txt", "w")
# try:
#     for x in range(n):
#         if x == 5:
#             raise RuntimeError("error: cannot process")
#         f.write(str(x**2) + "\n")
# except Exception as e:
#     print("Your request failed: ", e)
# finally:
#     f.close()


import contextlib


def my_generator(x):
    print("before")
    yield x ** 2
    print("in the middle")
    yield x ** 3
    print("after")
    return


gen = my_generator(10)
print(gen)

print("values in gen:")
for x in gen:
    print(x)

# print("before with")
# with my_generator(10) as x_squared:
#     print("inside with")
# print("after with")
