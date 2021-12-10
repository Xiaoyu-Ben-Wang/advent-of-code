from os import defpath
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    depths = [int(n) for n in f.read().split()]
    ans = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            ans +=1
    return ans


def partTwo(f):
    depths = [int(n) for n in f.read().split()]
    ans = 0
    for i in range(1, len(depths)-2):
        if sum(depths[i:i+3]) > sum(depths[i-1:i+2]):
            ans += 1
    return ans


if __name__ == '__main__':
    with open("1input.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
