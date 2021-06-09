import sys
import re

lst = []

with open('list.txt', 'a+') as MyFile:
    print('import complete')

with open('list.txt', 'r+') as MyFile:
    lst = [MyFile.read()]


def compare_and_add(x):
    if x in lst:
        return print('name already exists')
    else:
        lst.append(x)
    print("ok")


def compare_regular_expressions(x):
    regular = r'add ([a-zA-Z]+\s[a-zA-Z]+\s{0,1}([+][0-9]{12}){0,1})'
    if m := re.fullmatch(regular, x):
        return compare_and_add(m.group(1))
    else:
        print('wrong format')


while True:
    command = input("enter command or help:")
    if command == 'exit':
        MyFile = open('list.txt', 'w')
        for element in lst:
            MyFile.write(str(element)+'\n')
        sys.exit()
    elif "add" in command:
        compare_regular_expressions(command)
    elif command == 'status':
        print(*lst, sep='\n')
    elif command == 'help':
        print("""
        1.add <name> <secondname> - adds person with <firstname> and <lastname>
        2.exit - exit the program
        3.status -  list of added people
        """)
    else:
        print('Wrong command!')
