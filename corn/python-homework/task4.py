import sys
import re
from typing import List
lst=[]
def search(x):
            if x in lst: 
                return print('name already exists')
            else:
                lst.append(x)
                print("ok")   

while True:
    command = input("enter command or help:")  
    if command == 'exit':
        MyFile = open('list.txt','w')
        for element in lst:
            MyFile.write(str(element))
            MyFile.write('\n')
        sys.exit()    
    elif "add " in command:
        del_add = re.findall(r'add ([^..]+)', command)
        search(del_add)   
    elif command == 'status':
        print(*lst, sep='\n')   
    elif command == 'read': 
        MyFile = open('list.txt','r')   
        with open('list.txt','r') as MyFile:
            lst = [MyFile.read()]
            print('ok')
    elif command == 'help':
        print("""
        1.add <name> <secondname> - adds person with <firstname> and <lastname>
        2.exit - exit the program
        3.status -  list of added people
        4.read - reads people from a file
        """)
    else:
        print('Wrong command!')    
        
