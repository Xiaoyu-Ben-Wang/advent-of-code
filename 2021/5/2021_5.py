from timeit import default_timer as timer
from datetime import date, timedelta


def partOne(f):
    data = [line.split(' -> ') for line in f.read().splitlines()]
    for i, val in enumerate(data):
        data[i] = tuple([tuple(int(n) for n in val[0].split(',')), tuple(int(n) for n in val[1].split(','))])

    points = dict()

    for (x1,y1),(x2,y2) in data:
        if x1==x2:
            for i in range(min(y1,y2), max(y1,y2)+1, 1):
                points[(x1, i)] = points.get((x1, i), 0) + 1
        elif y1==y2:
            for i in range(min(x1, x2), max(x1, x2)+1, 1):
                points[(i, y1)] = points.get((i, y1), 0) + 1

    count = 0
    for val in points.values():
        if val > 1:
            count += 1
    return count

def partTwo(f):
    data = [line.split(' -> ') for line in f.read().splitlines()]
    for i, val in enumerate(data):
        data[i] = tuple([tuple(int(n) for n in val[0].split(',')), tuple(int(n) for n in val[1].split(','))])

    points = dict()

    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)+1):
                points[(x1, i)] = points.get((x1, i), 0) + 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)+1):
                points[(i, y1)] = points.get((i, y1), 0) + 1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            for x in range(x1, x2+1):
                y = (y1-y2)//(x1-x2)*(x-x1)+y1
                points[(x, y)] = points.get((x, y), 0) + 1

    count = 0
    for val in points.values():
        if val > 1:
            count += 1
    return count


if __name__ == '__main__':
    with open("5.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")