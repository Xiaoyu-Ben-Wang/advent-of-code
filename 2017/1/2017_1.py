from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    num = f.read().strip()
    ans = 0
    for i in range(len(num)):
        if num[i] == num[(i+1) % len(num)]:
            ans += int(num[i])
    return ans


def partTwo(f):
    num = f.read().strip()
    ans = 0
    for i in range(len(num)):
        if num[i] == num[(i+len(num)//2) % len(num)]:
            ans += int(num[i])
    return ans


if __name__ == '__main__':
    with open("1.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
