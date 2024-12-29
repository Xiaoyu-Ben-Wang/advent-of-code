from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    safe = 0
    for line in f.readlines():
        line = line.split()
        diffs = [int(line[i]) - int(line[i-1]) for i in range(1, len(line))]
        if len(diffs) == len(list(filter(lambda x: x >= 1 and x <= 3, diffs))) or len(diffs) == len(list(filter(lambda x: x <= -1 and x >= -3, diffs))):
            safe += 1
    return safe


def partTwo(f: TextIOWrapper):
    safe = 0
    for line in f.readlines():
        line = line.split()
        diffs = [int(line[i]) - int(line[i-1]) for i in range(1, len(line))]
        if len(diffs) == len(list(filter(lambda x: x >= 1 and x <= 3, diffs))) or len(diffs) == len(list(filter(lambda x: x <= -1 and x >= -3, diffs))):
            safe += 1
            continue
        for j in range(len(line)):
            newline = line.copy()
            newline.pop(j)
            diffs = [int(newline[i]) - int(newline[i-1]) for i in range(1, len(newline))]
            if len(diffs) == len(list(filter(lambda x: x >= 1 and x <= 3, diffs))) or len(diffs) == len(list(filter(lambda x: x <= -1 and x >= -3, diffs))):
                safe += 1
                break
    return safe


if __name__ == '__main__':
    with open('2024_2.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
