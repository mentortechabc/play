def add_name(names, new_name):
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
    pass


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