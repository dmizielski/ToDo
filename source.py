import json
import os
import counter

PATH = "C:/Users/xsemi/PycharmProjects/newProject/todo.json"
COUNTER_FILE = 'counter.json'
NO_FILE = 'File doesnt exists'
INVALID_INPUT = "Your input doesn't make any sense. Insert data again."
EMPTY_INPUT = 'You have to type something!'
EMPTY_FILE = "File is empty!"
INVALID_ID = "Task with this id doesn't exist!"
WRONG = "Something went wrong!"


def getTitle():
    title = ''
    while not title and not title.strip():
        title = input("Title: ")
    return title


def getDesc():
    desc = ''
    while not desc and not desc.strip():
        desc = input("Description: ")
    return desc


def getId():
    id_task = ''
    while not id_task and not id_task.strip():
        id_task = input("Task id: ")
    return id_task


def addTodo(title=getTitle(), description=getDesc(), path=PATH, path_counter=COUNTER_FILE):
    id_task = counter.readFile(path_counter)
    if os.path.exists(path):
        help_dict = getJson(path)
        help_dict[id_task] = {'Title': title, 'Description': description}
        with open(path, 'w') as pfile:
            json.dump(help_dict, pfile)
            counter.incValue(path_counter)
    else:
        todo_dict = {id_task: {'Title': title, 'Description': description}}
        with open(path, 'w') as pfile:
            json.dump(todo_dict, pfile)
            counter.incValue(path_counter)


def removeTodo(path=PATH):
    if not checkIfFileExists():
        return 0
    if checkIfFileIsEmpty():
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


def editTodo(title='', desc='', path=PATH):
    if not checkIfFileExists():
        return 0
    if checkIfFileIsEmpty():
        return 0
    update_dict = getJson(path)
    if not bool(update_dict):
        print('Dict is empty! You have to insert data!')
        return 0
    showTodo()
    task_id = getId()
    if task_id in update_dict:
        if not bool(title) and not bool(desc):
            title = getTitle()
            desc = getDesc()
        update_dict[task_id] = {'Title': title, 'Description': desc}
    else:
        print(f'{INVALID_ID}')
        return 0
    updateJson(update_dict, path)


def showTodo(path=PATH):
    if not checkIfFileExists():
        return 0
    if checkIfFileIsEmpty():
        return 0
    dictionary = getJson(path)
    for key, value in dictionary.items():
        print(f"ID: {key}")
        for content, content_value in value.items():
            print(f"{content}: {content_value}")
        print("-------------")
    return dictionary


def checkIfFileExists(path=PATH):
    if os.path.exists(path):
        return True
    print(f'File doesnt exists!')
    return False


def checkIfFileIsEmpty(path=PATH):
    if os.stat(path).st_size == 0:
        return True
    print(f'{EMPTY_FILE}')
    return False


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
