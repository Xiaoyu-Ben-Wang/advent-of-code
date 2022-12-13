from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    items = [(line[:len(line)//2], line[len(line)//2:]) for line in f.readlines()]
    total = 0
    for sacks in items:
        left, right = sacks
        left_set = set(left)
        right_set = set(right)

        for c in left_set:
            if c in right_set:
                if ord(c) >= ord('a') and ord(c) <= ord('z'):
                    total += ord(c) - ord('a')+1
                elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
                    total += ord(c) - ord('A')+27
    return total


def partTwo(f: TextIOWrapper):
    items = f.readlines()
    total = 0
    for i in range(0, len(items), 3):
        set1 = set(items[i])
        set2 = set(items[i+1])
        set3 = set(items[i+2])
        for c in set1:
            if c in set2 and c in set3:
                if ord(c) >= ord('a') and ord(c) <= ord('z'):
                    total += ord(c) - ord('a')+1
                elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
                    total += ord(c) - ord('A')+27
    return total


if __name__ == '__main__':
    with open('2022_3.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
