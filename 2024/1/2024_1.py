from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import heapq


def partOne(f: TextIOWrapper):
    left = []
    right = []
    for line in f.read().split('\n'):
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))
    heapq.heapify(left)
    heapq.heapify(right)
    dist = 0
    while len(left):
        dist += abs(heapq.heappop(left)-heapq.heappop(right))
    return dist


def partTwo(f: TextIOWrapper):
    left = []
    right = dict()
    for line in f.read().split('\n'):
        left.append(int(line.split()[0]))
        right[int(line.split()[1])] = right.get(int(line.split()[1]), 0) + 1
    similarity = 0
    for n in left:
        similarity += n * right.get(n, 0)
    return similarity


if __name__ == '__main__':
    with open('2023_1.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
