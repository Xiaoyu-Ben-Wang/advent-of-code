from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import math


def printBoard(positions, head, tail):
    for y in range(5):
        line = []
        for x in range(6):
            real_pos = (x, 4-y)
            if real_pos == tuple(head):
                line.append('H')
            elif real_pos == tuple(tail):
                line.append('T')
            elif real_pos in positions:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))


def partOne(f: TextIOWrapper):
    head = [0, 0]
    tail = [0, 0]

    positions = set()
    positions.add((0, 0))

    moves = [(x[0], int(x[1])) for x in [line.strip().split() for line in f.readlines()]]
    for d, n in moves:
        for _ in range(n):
            if d == 'L':
                head[0] -= 1
            elif d == 'R':
                head[0] += 1
            elif d == 'U':
                head[1] += 1
            elif d == 'D':
                head[1] -= 1

            if ((abs(head[0]-tail[0]) + abs(head[1] - tail[1])) == 3):
                if head[0] > tail[0]:
                    tail[0] += 1
                else:
                    tail[0] -= 1

                if head[1] > tail[1]:
                    tail[1] += 1
                else:
                    tail[1] -= 1
            elif abs(head[0]-tail[0]) == 2 or abs(head[1]-tail[1]) == 2:
                tail[0] = (tail[0]+head[0])//2
                tail[1] = (tail[1]+head[1])//2
            positions.add(tuple(tail))
            # printBoard(positions, head, tail)
            # print('='*20)
    return len(positions)


def partTwo(f: TextIOWrapper):
    knots = [[0, 0] for _ in range(10)]
    moves = [(x[0], int(x[1])) for x in [line.strip().split() for line in f.readlines()]]

    positions = set()
    positions.add((0, 0))
    for d, n in moves:
        for _ in range(n):
            if d == 'L':
                knots[0][0] -= 1
            elif d == 'R':
                knots[0][0] += 1
            elif d == 'U':
                knots[0][1] += 1
            elif d == 'D':
                knots[0][1] -= 1

            for i in range(9):
                head = knots[i]
                tail = knots[i+1]

                if ((abs(head[0]-tail[0]) + abs(head[1] - tail[1])) == 3):
                    if head[0] > tail[0]:
                        tail[0] += 1
                    else:
                        tail[0] -= 1

                    if head[1] > tail[1]:
                        tail[1] += 1
                    else:
                        tail[1] -= 1
                elif abs(head[0]-tail[0]) == 2 or abs(head[1]-tail[1]) == 2:
                    tail[0] = (tail[0]+head[0])//2
                    tail[1] = (tail[1]+head[1])//2
            positions.add(tuple(knots[-1]))
    return len(positions)
    pass


if __name__ == '__main__':
    with open('2022_9.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
