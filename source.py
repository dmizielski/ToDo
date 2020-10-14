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
    """
    Gets 'title' from user
    :return:
    string
    """
    title = ''
    while not title and not title.strip():
        title = input("Title: ")
    return title


def getDesc():
    """
    Gets 'desc' from user
    :return:
    string
    """
    desc = ''
    while not desc and not desc.strip():
        desc = input("Description: ")
    return desc


def getId():
    """
    Gets 'id' from user
    :return:
    string
    """
    id_task = ''
    while not id_task and not id_task.strip():
        id_task = input("Task id: ")
    return id_task


def addTodo(title=getTitle(), description=getDesc(), path=PATH, path_counter=COUNTER_FILE):
    """
    Adds task to the file\n
    :param title: title of task (optional)
    :param description: description of task (optional)
    :param path: directory where data will be saved
    :param path_counter: directory where id is stored
    :return:
    None
    """
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
    """
    Removes specified task by Id
    :param path: directory where data is stored
    :return:
    None
    """
    if not checkIfFileExists():
        return 0
    if checkIfFileIsEmpty():
        return 0
    remove_dict = getJson(path)
    if not bool(remove_dict):
        print('Dict is empty! You have to insert data!')
        return 0
    showTodo(path)
    task_id = getId()
    if task_id in remove_dict:
        remove_dict.pop(task_id)
        print(f'Task with ID:{task_id} has been deleted!')
    else:
        print(f'{INVALID_ID}')
        return 0
    updateJson(remove_dict, path)


def editTodo(title='', desc='', path=PATH):
    """
    Edits specified task by Id
    :param title: if left empty, prompts later
    :param desc: if left empty, prompts later
    :param path: directory where data is stored
    :return:
    None
    """
    if not checkIfFileExists(path):
        return 0
    if checkIfFileIsEmpty(path):
        return 0
    update_dict = getJson(path)
    if not bool(update_dict):
        print('Dict is empty! You have to insert data!')
        return 0
    showTodo(path)
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
    """
    View tasks
    :param path: directory where data is stored
    :return:
    None
    """
    if not checkIfFileExists(path):
        return 0
    if checkIfFileIsEmpty(path):
        return 0
    dictionary = getJson(path)
    for key, value in dictionary.items():
        print(f"ID: {key}")
        for content, content_value in value.items():
            print(f"{content}: {content_value}")
        print("-------------")


def checkIfFileExists(path=PATH):
    """
    Checks if file exists
    :param path: directory where file is supposed to be stored
    :return:
    Bool
    """
    if os.path.exists(path):
        return True
    print(f'File doesnt exists!')
    return False


def checkIfFileIsEmpty(path=PATH):
    """
    Checks if file is empty
    :param path: directory where file is stored
    :return:
    Bool
    """
    if os.stat(path).st_size == 0:
        print(f'{EMPTY_FILE}')
        return True
    return False


def updateJson(helpDict, path=PATH):
    """
    Updates .json file with new data
    :param helpDict: dictionary to be stored in file
    :param path: directory where file is stored
    :return:
    None
    """
    with open(path, 'w') as pfile:
        json.dump(helpDict, pfile)


def getJson(path=PATH):
    """
    Reads content of .json file
    :param path: directory where file is stored
    :return:
    Dict
    """
    if os.stat(path).st_size == 0:
        return {}
    else:
        with open(path, 'r') as pfile:
            help_dict = json.loads(pfile.read())
    return help_dict
