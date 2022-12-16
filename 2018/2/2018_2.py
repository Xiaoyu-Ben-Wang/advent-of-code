from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    two_count = 0
    three_count = 0
    for line in f.read().split('\n'):
        counter = dict()
        for c in line:
            counter[c] = counter.get(c, 0)+1
        if 2 in counter.values():
            two_count += 1
        if 3 in counter.values():
            three_count += 1
    return two_count * three_count


def count_diff(s1, s2):
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
    return diff


def partTwo(f: TextIOWrapper):
    boxes = [line.strip() for line in f.readlines()]

    for i in range(len(boxes)-1):
        for j in range(i+1, len(boxes)):
            if count_diff(boxes[i], boxes[j]) == 1:
                ans = []
                for pos, val in enumerate(boxes[i]):
                    if val == boxes[j][pos]:
                        ans.append(val)
                return ''.join(ans)


if __name__ == '__main__':
    with open('2018_2.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
