import json
import os


class Counter:
    count = 0


def readFile():
    if not os.path.exists('counter.json'):
        with open('counter.json', 'w') as pfile:
            json.dump(Counter.count, pfile)
    with open('counter.json', 'r') as pfile:
        Counter.count = json.load(pfile)
    return Counter.count


def incValue():
    Counter.count += 1
    with open('counter.json', 'w') as pfile:
        json.dump(Counter.count, pfile)
