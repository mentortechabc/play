# На вход поступает число в виде аргумента командной строки;
# На экран вывести квадратный корень это числа (почитать в документации / найти в интернете как).


import math


def calculate_square_root(number):
    return round(math.sqrt(number), 3)


def is_input_number(user_input):
    """
    This function returns True if user_input is a number
    """
    return user_input.isdigit()


def main():
    user_input = input(
        "Enter a positive number to calculate the square root of it \n")
    if is_input_number(user_input):
        square_root = calculate_square_root(int(user_input))
        print(square_root)
    else:
        print(
            "You entered '{0}'. This is not a positive number.".format(user_input))


main()
