from timeit import default_timer as timer
from datetime import timedelta
from progress.bar import Bar


def partOne(f):
    data = [[int(n) for n in line] for line in f.read().splitlines()]
    return dijsktra(data)


def addRisk(n, offset):
    n += offset
    if n > 9:
        n = n-9
    return n


def partTwo(f):
    data = [[int(n) for n in line] for line in f.read().splitlines()]
    for i in range(len(data)):
        extendRow = []
        for offset in range(1, 5):
            extendRow.extend([addRisk(num, offset) for num in data[i]])
        data[i].extend(extendRow)

    newRows = []
    for offset in range(1, 5):
        for i in range(len(data)):
            newRows.append([addRisk(num, offset) for num in data[i]])
    data.extend(newRows)

    return dijsktra(data)


def isValidPoint(i, j, rows, cols):
    return i >= 0 and j >= 0 and i < rows and j < cols


def dijsktra(graph):
    weights = [line.copy() for line in graph]
    temp = set()
    permanent = set()
    graph[0][0] = 0

    for m in range(len(graph)):
        for n in range(len(graph)):
            graph[m][n] = float('inf')
    graph[0][0] = 0
    i, j = 0, 0

    bar = Bar('Searching', max=len(graph)*len(graph[0]))
    bar.next()

    while True:
        permanent.add((i, j))
        points = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for x, y in points:
            if isValidPoint(x, y, len(graph), len(graph[0])) and (x, y) not in permanent:
                if (x, y) not in temp:
                    temp.add((x, y))
                graph[x][y] = min(graph[x][y], weights[x][y]+graph[i][j])

        minVal = float('inf')
        for x, y in temp:
            if graph[x][y] < minVal:
                i, j = x, y
                minVal = graph[x][y]
        if (i, j) in temp:
            temp.remove((i, j))

        if i == len(graph)-1 and j == len(graph[0])-1:
            bar.next()
            bar.finish()
            return graph[i][j]
        bar.next()


if __name__ == '__main__':
    with open('15.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
