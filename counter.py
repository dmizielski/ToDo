import json
import os

PATH = 'counter.json'


class Counter:
    count = 0


def readFile(path):
    if not os.path.exists(path):
        with open(path, 'w') as pfile:
            json.dump(Counter.count, pfile)
    with open(path, 'r') as pfile:
        Counter.count = json.load(pfile)
    return int(Counter.count)


def incValue(path):
    Counter.count += 1
    with open(path, 'w') as pfile:
        json.dump(Counter.count, pfile)
