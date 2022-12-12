import os
import time
from datetime import timedelta
from io import TextIOWrapper
from timeit import default_timer as timer


class COLOR:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getVal(char):
    if ord(char) >= ord('a') and ord(char) <= ord('z'):
        return ord(char)-ord('a')
    return char


def validJumpPart1(a, b):
    return b-a <= 1
    

def validJumpPart2(a, b):
    return a-b <= 1


def getPathStr(graph, visited):
    output = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if (i, j) in visited:
                output.append(COLOR.OKGREEN +
                              chr(graph[i][j]+ord('a')) + COLOR.ENDC)
            else:
                output.append(chr(graph[i][j]+ord('a')))
        output.append('\n')
    return ''.join(output)


def partOne(f: TextIOWrapper):
    graph = [[getVal(char) for char in line.strip()] for line in f.readlines()]

    start = None
    end = None

    visited = set()

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'S':
                start = (i, j)
                graph[i][j] = 0
            elif graph[i][j] == 'E':
                end = (i, j)
                graph[i][j] = 25

    visited = set()
    queue = set()
    queue.add(start)
    distance = 0
    while True:
        new_queue = set()
        for point in queue:
            visited.add(point)
        for point in queue:
            if point == end:
                return distance

            row, col = point
            if row > 0 and (row-1, col) not in visited and validJumpPart1(graph[row][col], graph[row-1][col]):
                new_queue.add((row-1, col))

            if row < len(graph)-1 and (row+1, col) not in visited and validJumpPart1(graph[row][col], graph[row+1][col]):
                new_queue.add((row+1, col))

            if col > 0 and (row, col-1) not in visited and validJumpPart1(graph[row][col], graph[row][col-1]):
                new_queue.add((row, col-1))

            if col < len(graph[row])-1 and (row, col+1) not in visited and validJumpPart1(graph[row][col], graph[row][col+1]):
                new_queue.add((row, col+1))

        queue = new_queue
        # os.system('clear||cls')
        # print(getPathStr(graph, visited))
        # print(f'{len(visited)}/{sum(len(r) for r in graph)}')

        distance += 1


def partTwo(f: TextIOWrapper):
    graph = [[getVal(char) for char in line.strip()] for line in f.readlines()]

    start = (0, 0)

    visited = set()

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'S':
                graph[i][j] = 0
            elif graph[i][j] == 'E':
                start = (i, j)
                graph[i][j] = 25

    visited = set()
    queue = set()
    queue.add(start)
    distance = 0
    while True:
        new_queue = set()
        for point in queue:
            visited.add(point)
        for point in queue:
            row, col = point
            if graph[row][col] == 0:
                return distance

            if row > 0 and (row-1, col) not in visited and validJumpPart2(graph[row][col], graph[row-1][col]):
                new_queue.add((row-1, col))

            if row < len(graph)-1 and (row+1, col) not in visited and validJumpPart2(graph[row][col], graph[row+1][col]):
                new_queue.add((row+1, col))

            if col > 0 and (row, col-1) not in visited and validJumpPart2(graph[row][col], graph[row][col-1]):
                new_queue.add((row, col-1))

            if col < len(graph[row])-1 and (row, col+1) not in visited and validJumpPart2(graph[row][col], graph[row][col+1]):
                new_queue.add((row, col+1))

        queue = new_queue
        # os.system('clear||cls')
        # print(getPathStr(graph, visited))
        # print(f'{len(visited)}/{sum(len(r) for r in graph)}')

        distance += 1


if __name__ == '__main__':
    with open('2022_12.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
