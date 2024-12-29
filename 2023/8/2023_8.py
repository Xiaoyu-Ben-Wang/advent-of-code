from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import re


def partOne(f: TextIOWrapper):
    directions, nodes = f.read().split('\n\n')
    node_map = {}
    for node in nodes.split('\n'):
        arr = re.findall(r'(\w+)', node)
        node_map[arr[0]] = (arr[1], arr[2])
    pos = 'AAA'
    goal = 'ZZZ'
    i = 0
    steps = 0
    while pos != goal:
        if directions[i] == 'L':
            pos = node_map[pos][0]
        elif directions[i] == 'R':
            pos = node_map[pos][1]
        else:
            raise Exception('something went wrong: ' + directions[i])
        steps += 1
        i = (i+1) % len(directions)
    return steps


def partTwo(f: TextIOWrapper):
    directions, nodes = f.read().split('\n\n')
    node_map = {}
    for node in nodes.split('\n'):
        arr = re.findall(r'(\w+)', node)
        node_map[arr[0]] = (arr[1], arr[2])
    pos = [p for p in node_map.keys() if p[-1] == 'A']

    for p in pos:
        location = p
        i = 0
        seen = {}
        steps = 0
        while True:
            seen[location] = steps
            if directions[i] == 'L':
                location = node_map[location][0]
            elif directions[i] == 'R':
                location = node_map[location][1]
            if location in seen:
                print(location)
                print(seen[location])
                print(steps)
                break
            steps += 1
            i = (i+1) % len(directions)
            if p == location:
                break


if __name__ == '__main__':
    with open('2023_8.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
