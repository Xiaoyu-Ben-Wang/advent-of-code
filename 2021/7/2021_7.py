from timeit import default_timer as timer
from datetime import timedelta
import math

def partOne(f):
    positions = [int(n) for n in f.read().strip().split(',')]
    min_pos = min(positions)
    max_pos = max(positions)

    minFuel = math.inf
    minPos = None
    for i in range(min_pos, max_pos+1):
        fuel = 0
        for p in positions:
            fuel += abs(p-i)
        if not minPos or fuel < minFuel:
            minFuel = fuel
            minPos = i
    return minFuel


def partTwo(f):
    positions = [int(n) for n in f.read().strip().split(',')]
    min_pos = min(positions)
    max_pos = max(positions)

    minFuel = math.inf
    minPos = None
    for i in range(min_pos, max_pos+1):
        fuel = 0
        for p in positions:
            n = abs(p-i)
            fuel += n*(n+1)//2
        if not minPos or fuel < minFuel:
            minFuel = fuel
            minPos = i
    return minFuel


if __name__ == '__main__':
    with open('7.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')