from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta

import re

def partOne(f: TextIOWrapper):
    PATTERN = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    claimed = set()
    overlap = set()

    for line in f.readlines():
        cid, x, y, width, height = [int(n) for n in re.findall(PATTERN, line.strip())[0]]
        
        for i in range(x, x+width):
            for j in range(y, y+height):
                point = (i,j)
                if point in claimed:
                    overlap.add(point)
                else:
                    claimed.add(point)
    return len(overlap)


def partTwo(f: TextIOWrapper):
    PATTERN = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
    claimed = set()
    overlap = set()

    claims = f.readlines()

    for line in claims:
        cid, x, y, width, height = [int(n) for n in re.findall(PATTERN, line.strip())[0]]
        
        for i in range(x, x+width):
            for j in range(y, y+height):
                point = (i,j)
                if point in claimed:
                    overlap.add(point)
                else:
                    claimed.add(point)

    for line in claims:
        cid, x, y, width, height = [int(n) for n in re.findall(PATTERN, line.strip())[0]]

        has_overlap = False

        for i in range(x, x+width):
            for j in range(y, y+height):
                point = (i,j)
                if point in overlap:
                    has_overlap = True
        if not has_overlap:
            return cid


if __name__ == '__main__':
    with open('2018_3.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')