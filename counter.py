import json
import os

PATH = 'counter.json'


class Counter:
    count = 0


def readFile(path=PATH):
    """
    Reads value from file or creates file with Counter.counter attr
    :param path:
    :return:
    int
    """
    if not os.path.exists(path):
        with open(path, 'w') as pfile:
            json.dump(Counter.count, pfile)
    with open(path, 'r') as pfile:
        Counter.count = json.load(pfile)
    return int(Counter.count)


def incValue(path=PATH):
    """
    Increments value of Counter.counter by 1
    :param path:
    :return:
    """
    Counter.count += 1
    with open(path, 'w') as pfile:
        json.dump(Counter.count, pfile)
