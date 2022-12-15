from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    paths = [[(int(pair.split(',')[0]), int(pair.split(',')[1])) for pair in arr] for arr in [line.strip().split(' -> ') for line in f.readlines()]]
    wall = set()
    sand = set()
    for path in paths:
        for i in range(len(path)-1):
            start = path[i]
            end = path[i+1]

            if start[0] == end[0]:
                small = min(start[1], end[1])
                big = max(start[1], end[1])
                for n in range(small, big+1):
                    wall.add((start[0], n))
            elif start[1] == end[1]:
                small = min(start[0], end[0])
                big = max(start[0], end[0])
                for n in range(small, big+1):
                    wall.add((n, start[1]))

    lowest_points = dict()
    for x,y in wall:
        lowest_points[x] = max(y, lowest_points.get(x, float('-inf')))

    source = (500, 0)
    while source not in sand:
        x,y = source
        while True:
            next_poss = [(x, y+1), (x-1, y+1), (x+1, y+1)]
            settled = True
            for pos in next_poss:
                if pos not in wall and pos not in sand:
                    x,y = pos
                    settled = False
                    break

            if settled:
                sand.add((x,y))
                break
            if x not in lowest_points or lowest_points[x] < y:
                return len(sand)


def partTwo(f: TextIOWrapper):
    paths = [[(int(pair.split(',')[0]), int(pair.split(',')[1])) for pair in arr] for arr in [line.strip().split(' -> ') for line in f.readlines()]]
    wall = set()
    sand = set()
    for path in paths:
        for i in range(len(path)-1):
            start = path[i]
            end = path[i+1]

            if start[0] == end[0]:
                small = min(start[1], end[1])
                big = max(start[1], end[1])
                for n in range(small, big+1):
                    wall.add((start[0], n))
            elif start[1] == end[1]:
                small = min(start[0], end[0])
                big = max(start[0], end[0])
                for n in range(small, big+1):
                    wall.add((n, start[1]))

    max_y = -1
    for x,y in wall:
        max_y = max(y, max_y)
    max_y += 2

    source = (500, 0)
    while source not in sand:
        x,y = source
        while True:
            next_poss = [(x, y+1), (x-1, y+1), (x+1, y+1)]
            settled = True
            for pos in next_poss:
                if pos not in wall and pos not in sand and pos[1] < max_y:
                    x,y = pos
                    settled = False
                    break
            
            if settled:
                sand.add((x,y))
                break
    return len(sand)


if __name__ == '__main__':
    with open('2022_14.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')