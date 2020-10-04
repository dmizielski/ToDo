import json
import os
from counter import readFile, incValue

PATH = "C:/Users/xsemi/PycharmProjects/newProject/todo.json"
FILE = "todo.json"
INVALID_INPUT = "Your input doesn't make any sense"
EMPTY_FILE = "File is empty!"
INVALID_ID = "Task with this id doesn't exist!"


def addTodo(title, description):
    id = int(readFile())
    if os.path.exists(PATH):
        helpDict = getJson()
        helpDict[id] = {'Title': title, 'Description': description}
        with open(FILE, 'w') as pfile:
            json.dump(helpDict, pfile)
            incValue()
    else:
        todoDict = {'Title': title, 'Description': description}
        helpDict = {id: todoDict}
        with open(FILE, 'w') as pfile:
            json.dump(helpDict, pfile)
            incValue()


def insertData():
    validData = False
    while not validData:
        try:
            title = str(input("Title: "))
            desc = str(input("Description: "))
            addTodo(title, desc)
            validData = True
        except TypeError:
            print(f"{INVALID_INPUT}")


def removeTodo():
    checkIfFileExists()
    checkIfFileIsEmpty()
    try:
        showTodo()
        id = str(input("Which task you want to delete?"))
        #TODO To finish
    except TypeError:
        print(f"{INVALID_ID}")


def checkIfFileExists():
    if not os.path.exists(PATH):
        raise FileNotFoundError


def checkIfFileIsEmpty():
    if os.stat(PATH).st_size == 0:
        raise EMPTY_FILE

#TODO editTODO
def editTodo(todoDict):
    pass


def showTodo():
    checkIfFileExists()
    checkIfFileIsEmpty()
    dictionary = getJson()
    for key, value in dictionary.items():
        print(f"ID: {key}")
        for content, content_value in value.items():
            print(f"{content}: {content_value}")
        print("-------------")
    #TODO Check if showTODO works with individual functions


def getJson():
    if os.stat(PATH).st_size == 0:
        return {}
    else:
        with open(FILE, 'r') as pfile:
            helpDict = json.loads(pfile.read())
    return helpDict
