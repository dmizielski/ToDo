import json


class Counter:
    count = 0


def readFile():
    with open('counter.json', 'r') as pfile:
        Counter.count = json.load(pfile)
    return Counter.count


def incValue():
    Counter.count += 1
    with open('counter.json', 'w') as pfile:
        json.dump(Counter.count, pfile)
