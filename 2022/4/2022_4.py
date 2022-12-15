from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    section_pairs = [([int(n) for n in section[0].split('-')], [int(n) for n in section[1].split('-')]) for section in [line.strip().split(',') for line in f.readlines()]]
    count = 0
    for left, right in section_pairs:
        if (left[0] >= right[0] and left[1] <= right[1]):
            count += 1
        elif (left[0] <= right[0] and left[1] >= right[1]):
            count += 1
    return count


def partTwo(f: TextIOWrapper):
    section_pairs = [([int(n) for n in section[0].split('-')], [int(n) for n in section[1].split('-')]) for section in [line.strip().split(',') for line in f.readlines()]]
    count = 0
    for left, right in section_pairs:
        if (left[0] > right[1]):
            continue
        elif (left[1] < right[0]):
            continue
        count += 1
    return count


if __name__ == '__main__':
    with open('2022_4.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
