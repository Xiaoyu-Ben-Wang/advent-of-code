from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    inst = [int(i) for i in f.read().strip().split('\n')]
    p = 0
    steps = 0
    while p >= 0 and p < len(inst):
        move = inst[p]
        inst[p] += 1
        p += move
        steps += 1
    return steps




def partTwo(f):
    inst = [int(i) for i in f.read().strip().split('\n')]
    p = 0
    steps = 0
    while p >= 0 and p < len(inst):
        move = inst[p]
        if move >= 3:
            inst[p] -= 1
        else:
            inst[p] += 1
        p += move
        steps += 1
    return steps


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