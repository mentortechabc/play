import sys
command_list = """commands:
 add [first name] [last name]: add in data base
 status: view sorted name-list
 exit: finish program
 help: command list
 clear: clear the list
"""

print('enter help for details or any command')
while True:
    sys.stdout.flush()
    input_str = sys.stdin.readline()
    input_list = input_str.split(' ')
    if input_list[0] == 'add':
        if len(input_list) == 3:
            sys.stdout.flush()
            read_list = open("list.txt", "r")
            if " ".join(input_list[1:]).title() in read_list.read():
                #  ar.read().find(" ".join(input_list[1:]).title()) != -1 :
                print("the Name has been added already")
                read_list.close()
            else:
                add = open("list.txt", "a")
                add.write(" ".join(input_list[1:]).title())
                print('OK')
                add.close()
        else:
            print("enter in the format: add {First name} {Last name}")
    elif input_str == 'help\n':
        print(command_list)
    elif input_str == 'status\n':
        r = open("list.txt", "r")
        list_file = r.read().splitlines()
        print("\n".join(sorted(list_file)))
        r.close()
    elif input_str == 'clear\n':
        w = open("list.txt", "w")
        w.close()
    elif input_str == 'exit\n':
        break
    else:
        print('Unknown command. enter [help] for more information')
