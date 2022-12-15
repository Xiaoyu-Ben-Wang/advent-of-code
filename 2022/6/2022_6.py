from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    content = f.read().strip()
    for i in range(0, len(content)-4):
        if len(set(content[i:i+4])) == 4:
            return i+4


def partTwo(f: TextIOWrapper):
    content = f.read().strip()
    for i in range(0, len(content)-14):
        if len(set(content[i:i+14])) == 14:
            return i+14


if __name__ == '__main__':
    with open('2022_6.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
