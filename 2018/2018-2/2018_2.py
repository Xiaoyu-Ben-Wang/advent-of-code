from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    pass


def partTwo(f):
    pass


if __name__ == '__main__':
    with open("input.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        start = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
