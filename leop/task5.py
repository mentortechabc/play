# Как вариант сделала класс Names,
# где функция def add_name выполняет проверку
# перед добавлением элемента в класс

class Names:

    def __init__(self, names_list):
        self.__names_list = names_list

    def add_name(self, new_name):
        if new_name in self.__names_list:
            return False
        else:
            self.__names_list.append(new_name)
            self.__names_list.sort()
            return True

    @property
    def list(self):
        return self.__names_list


def test_add_name_class():
    names_list = Names(['bob', 'mike'])

    assert names_list.add_name('vasya') is True
    assert names_list.add_name('bob') is False
    assert names_list.list[0] == 'bob'
    assert names_list.list[1] == 'mike'
    assert names_list.list[2] == 'vasya'

    print(names_list.list)


"""
    names is a list of strings, new_name is a string.

    add_name checks if the `new_name` is in the list.

    If it is not in the list:
      * the `new_name` is added to the list
      * the list is sorted
      * function returns True

    if it is in the list the function returns False and exits
    """

# put your code here
# Вот решение в виде функции :)


def add_name(names_list: list, new_name: str) -> bool:
    if new_name in names_list:
        return False
    else:
        names_list.append(new_name)
        names_list.sort()
        return True


def test_add_name():
    # don't change this function
    lst = ['bob', 'mike']

    assert add_name(lst, 'bob') is False
    assert lst == ['bob', 'mike']

    assert add_name(lst, 'ann') is True
    assert lst == ['ann', 'bob', 'mike']

    assert add_name(lst, 'ann') is False
    assert lst == ['ann', 'bob', 'mike']


if __name__ == '__main__':
    test_add_name()
    test_add_name_class()
