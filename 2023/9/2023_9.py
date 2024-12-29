from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    def isZeroes(arr):
        for n in arr:
            if n != 0:
                return False
        return True
    total = 0

    for line in f.read().split('\n'):
        line = line.split(' ')
        diffs = [int(line[-1])]
        diff = line
        while not isZeroes(diff):
            diff = [int(diff[i])-int(diff[i-1]) for i in range(1, len(diff))]
            diffs.append(diff[-1])
        total += sum(diffs)
    return total


def partTwo(f: TextIOWrapper):
    def isZeroes(arr):
        for n in arr:
            if n != 0:
                return False
        return True
    total = 0

    for line in f.read().split('\n'):
        line = line.split(' ')
        diffsFront = [int(line[0])]
        diffsEnd = [int(line[-1])]
        diff = line
        while not isZeroes(diff):
            diff = [int(diff[i])-int(diff[i-1]) for i in range(1, len(diff))]
            diffsEnd.append(diff[-1])
            diffsFront.append(diff[0])
        total += sum([-n for n in diffsFront])
        total += sum(diffsEnd)
    return total


if __name__ == '__main__':
    with open('2023_9.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
