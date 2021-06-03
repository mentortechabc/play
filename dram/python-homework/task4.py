import sys

while True:
    if sys.stdin.read(3) == 'add':
        ar = open("list.txt", "a+")
        ar.write(sys.stdin.readline())
        ar.close()
        print('OK')
    elif sys.stdin.read(6) == 'status':
        r = open("list.txt", "r")
        print(r.read())
    elif sys.stdin.read(4) == 'exit':
        break
    else :
        print('unknown command')