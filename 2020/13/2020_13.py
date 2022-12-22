from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    inp = f.read().splitlines()
    timestamp = int(inp[0])
    ids = [int(n) for n in inp[1].split(',') if n != 'x']

    lowest_diff = 1000
    lowest_id = -1
    for bid in ids:

        if bid*(timestamp//bid)+bid-timestamp < lowest_diff:
            lowest_diff = bid*(timestamp//bid)+bid-timestamp
            lowest_id = bid
    return lowest_diff*lowest_id


def partTwo(f: TextIOWrapper):
    inp = f.read().splitlines()
    timestamp = int(inp[0])
    ids = [int(n) if n != 'x' else n for n in inp[1].split(',')]

    for i, val in enumerate(ids):


if __name__ == '__main__':
    with open('2020_13.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
