from timeit import default_timer as timer
from datetime import timedelta
from typing import Set


def calculatePolymer(instructions, template, count):
    pairCounter = dict()
    charCounter = dict()
    for i in range(len(template)-1):
        key = tuple(template[i:i+2])
        pairCounter[key] = pairCounter.get(key, 0) + 1
    for c in template:
        charCounter[c] = charCounter.get(c, 0)+1

    for i in range(count):
        newCounter = pairCounter.copy()
        for ins in instructions:
            between = tuple(ins[0])
            addChar = ins[1]
            if between in pairCounter:
                oldCount = pairCounter[between]
                newCounter[between] = newCounter.get(between) - oldCount
                newCounter[(between[0], addChar)] = newCounter.get((between[0], addChar), 0) + oldCount
                newCounter[(addChar, between[1])] = newCounter.get((addChar, between[1]), 0) + oldCount
                charCounter[addChar] = charCounter.get(addChar, 0) + oldCount
        pairCounter = newCounter.copy()

    return max(charCounter.values())-min(charCounter.values())



def partOne(f):
    STEPS = 10

    data = f.read().split('\n\n')
    template = list(data[0].strip())
    instructions = data[1].splitlines()
    for i, val in enumerate(instructions):
        instructions[i] = tuple(val.split(' -> '))

    return calculatePolymer(instructions, template, STEPS)


def partTwo(f):
    STEPS = 40

    data = f.read().split('\n\n')
    template = list(data[0].strip())
    instructions = data[1].splitlines()
    for i, val in enumerate(instructions):
        instructions[i] = tuple(val.split(' -> '))

    return calculatePolymer(instructions, template, STEPS)


if __name__ == '__main__':
    with open('14.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
