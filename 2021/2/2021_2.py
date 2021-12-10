from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    directions = [ins for ins in f.read().split('\n')]
    depth = 0
    horizontal = 0
    for d in directions:
        d = d.split()
        if d[0]=='forward':
            horizontal += int(d[1])
        elif d[0] =='down':
            depth += int(d[1])
        elif d[0] == 'up':
            depth -= int(d[1])
    return depth * horizontal


def partTwo(f):
    directions = [ins for ins in f.read().split('\n')]
    depth = 0
    horizontal = 0
    aim = 0
    for d in directions:
        d = d.split()
        if d[0] == 'forward':
            horizontal += int(d[1])
            depth += aim*int(d[1])
        elif d[0] == 'down':
            aim += int(d[1])
        elif d[0] == 'up':
            aim -= int(d[1])
    return depth * horizontal


if __name__ == '__main__':
    with open("2input.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
