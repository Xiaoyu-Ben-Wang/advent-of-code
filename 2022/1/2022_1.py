from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    return max([sum([int(item.strip() or 0) for item in group.split()]) for group in f.read().split('\n\n')])


def partTwo(f: TextIOWrapper):
    return sum(sorted([sum([int(item.strip() or 0) for item in group.split()]) for group in f.read().split('\n\n')])[-3:])


if __name__ == '__main__':
    with open('2022_1.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
