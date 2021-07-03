from typing import List, Dict, Union


def get_x():
    return 100


def get_y():
    return 200


class YourClass:
    pass


Mytype = List[Dict[int, List[int]]]


def f(x: 'str', y: Dict[int, str]) -> YourClass:
    return YourClass()


x = get_x()
y = get_y()
d = {"asdas": YourClass()}
d = {}
result = f(12, d)
result = f("12", d)
result = f({}, d)

print(result)
exit(0)

from typing import Dict, Callable


def fn(x: int, y: int) -> str:
    return f"{x}..{y}"


def fn2(x: int, y: int) -> int:
    return 123


def process_dict(d: Dict) -> Dict:
    return {k: v * 2 for k, v in d.items()}


def process_dict_with_callable(d: Dict[int, float], f: Callable[[float], float]) -> Dict:
    return {k: f(v) for k, v in d.items()}


# res: float = fn(12, 23) * 1.2
# print(res)
#
# process_dict([1, 2, 3])

# res = process_dict_with_callable({"asd": 2.2, "123": 5}, lambda x: x ** 2)
# res = process_dict_with_callable({2: 2.2, 1: 5}, lambda x: x ** 2)
# print (res)
