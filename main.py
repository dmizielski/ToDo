from source import removeTodo, showTodo, editTodo, insertData


if __name__ == '__main__':
    while True:
        print("#" * 50)
        print("1 - add new task\n2 - remove specified task\n3 - edit specified task\n4 - view all tasks\n5 - exit")
        user_input = int(input("What do you want to do?\n"))
        if user_input == 1:
            insertData()
        elif user_input == 2:
            removeTodo()
        elif user_input == 3:
            editTodo()
        elif user_input == 4:
            showTodo()
        elif user_input == 5:
            exit()
