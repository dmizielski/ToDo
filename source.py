import json
import os
from counter import readFile, incValue

PATH = "C:/Users/xsemi/PycharmProjects/newProject/todo.json"
FILE = "todo.json"
INVALID_INPUT = "Your input doesn't make any sense. Insert data again."
EMPTY_FILE = "File is empty!"
INVALID_ID = "Task with this id doesn't exist!"
WRONG = "Something went wrong!"


def insertData():
    valid_data = False
    while not valid_data:
        title = str(input("Title: "))
        desc = str(input("Description: "))
        if title.isdigit() or desc.isdigit():
            print(f"{INVALID_INPUT}")
        addTodo(title, desc)
        valid_data = True


def addTodo(title, description):
    id = int(readFile())
    if os.path.exists(PATH):
        help_dict = getJson(PATH)
        help_dict[id] = {'Title': title, 'Description': description}
        with open(FILE, 'w') as pfile:
            json.dump(help_dict, pfile)
            incValue()
    else:
        todo_dict = {'Title': title, 'Description': description}
        help_dict = {id: todo_dict}
        with open(FILE, 'w') as pfile:
            json.dump(help_dict, pfile)
            incValue()


def removeTodo(path=PATH):
    if not checkIfFileExists():
        print(f'File doesnt exists!')
        return 0
    if checkIfFileIsEmpty():
        print(f'{EMPTY_FILE}')
        return 0
    remove_dict = getJson(path)
    if not bool(remove_dict):
        print('Dict is empty! You have to insert data!')
        return 0
    showTodo()
    task_id = str(input("Which task you want to delete?\n"))
    if task_id in remove_dict:
        remove_dict.pop(task_id)
        print(f'Task with ID:{task_id} has been deleted!')
    else:
        print(f'{INVALID_ID}')
        return 0
    updateJson(remove_dict, path)


def checkIfFileExists(path=PATH):
    if os.path.exists(path):
        return True
    return False


def checkIfFileIsEmpty(path=PATH):
    if os.stat(path).st_size == 0:
        return True
    return False


def editTodo(path=PATH):
    if not checkIfFileExists():
        print(f'File doesnt exists!')
        return 0
    if checkIfFileIsEmpty():
        print(f'{EMPTY_FILE}')
        return 0
    update_dict = getJson(path)
    if not bool(update_dict):
        print('Dict is empty! You have to insert data!')
        return 0
    showTodo()
    task_id = str(input("Which task you want to modify?\n"))
    if task_id in update_dict:
        title = str(input("Title: "))
        desc = str(input("Description: "))
        update_dict[task_id] = {'Title': title, 'Description': desc}
    else:
        print(f'{INVALID_ID}')
        return 0
    updateJson(update_dict, path)


def showTodo(path=PATH):
    checkIfFileExists()
    checkIfFileIsEmpty()
    dictionary = getJson(path)
    for key, value in dictionary.items():
        print(f"ID: {key}")
        for content, content_value in value.items():
            print(f"{content}: {content_value}")
        print("-------------")
    return dictionary


def updateJson(helpDict, path=PATH):
    with open(path, 'w') as pfile:
        json.dump(helpDict, pfile)


def getJson(path):
    if os.stat(path).st_size == 0:
        return {}
    else:
        with open(path, 'r') as pfile:
            help_dict = json.loads(pfile.read())
    return help_dict
