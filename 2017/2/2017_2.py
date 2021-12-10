from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    rows = f.read().strip().split('\n')
    checksum = 0
    for r in rows:
        nums = [int(n) for n in r.split()]
        checksum += max(nums)-min(nums)
    return checksum


def partTwo(f):
    rows = f.read().strip().split('\n')
    ans = 0
    for r in rows:
        nums = [int(n) for n in r.split()]
        for i in nums:
            for j in nums:
                if i > j and i % j ==0:
                    ans += i // j
    return ans


if __name__ == '__main__':
    with open("2.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")