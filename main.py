from source import addTodo, removeTodo, showTodo, editTodo, insertData
from collections import defaultdict
from counter import readFile


if __name__ == '__main__':
    # while True:
    #     print("1 - add new task\n2 - remove specified task\n3 - edit specified task\n4 - view all tasks")
    #     userinput = int(input("What do you want to do?\n"))
    #     if userinput == 1:
    #         insertData()
    #     elif userinput == 2:
    #         print('you choosed 2')
    #     elif userinput == 3:
    #         print('you choosed 3')
    #     elif userinput == 4:
    #         print('exit')
    #         exit()
    showTodo()
