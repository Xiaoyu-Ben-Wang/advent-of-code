from timeit import default_timer as timer
from datetime import timedelta


def flash(arr):
    flasedList = set()
    # increase all by 1
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[i])-1):
            arr[i][j] += + 1
    # determine flashes
    while True:
        flashOccured = False
        for i in range(1, len(arr)-1):
            for j in range(1, len(arr[i])-1):
                if arr[i][j] > 9 and (i, j) not in flasedList:
                    points = [(i-1, j), (i-1, j-1), (i-1, j+1), (i+1, j), (i+1, j-1), (i+1, j+1), (i, j-1), (i, j+1)]
                    for p in points:
                        arr[p[0]][p[1]] += 1
                    flashOccured = True
                    flasedList.add((i, j))
        if not flashOccured:
            break
    # set to zero
    for p in flasedList:
        arr[p[0]][p[1]] = 0

    return len(flasedList)


def partOne(f):
    data = [[int(n) for n in line] for line in f.read().splitlines()]
    data.insert(0, [0 for _ in range(len(data[0]))])
    data.append([0 for _ in range(len(data[0]))])
    for line in data:
        line.insert(0, 0)
        line.append(0)
    count = 0
    for i in range(100):
        count += flash(data)
    return count


def partTwo(f):
    data = [[int(n) for n in line] for line in f.read().splitlines()]
    data.insert(0, [0 for _ in range(len(data[0]))])
    data.append([0 for _ in range(len(data[0]))])
    for line in data:
        line.insert(0, 0)
        line.append(0)
    count = 0
    for i in range(500):
        if flash(data) == (len(data)-2)*(len(data[0])-2):
            return i+1


if __name__ == '__main__':
    with open('11.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
