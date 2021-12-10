from timeit import default_timer as timer
from datetime import timedelta
import hashlib


def partOne(key):
    i = 0
    while True:
        string = key+str(i)
        if hashlib.md5(string.encode()).hexdigest()[:5] == '00000':
            return i
        i += 1


def partTwo(key):
    i = 0
    while True:
        string = key+str(i)
        if hashlib.md5(string.encode()).hexdigest()[:6] == '000000':
            return i
        i += 1


if __name__ == '__main__':
    puzzle_key = 'iwrupvqb'

    start = timer()
    ans = partOne(puzzle_key)
    end = timer()
    print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
    start = timer()
    ans = partTwo(puzzle_key)
    end = timer()
    print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
