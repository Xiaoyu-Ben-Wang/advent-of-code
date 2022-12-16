from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    wires = f.read().strip().split('\n')
    wire1 = wires[0].split(',')
    wire2 = wires[1].split(',')
    points1 = set()
    points2 = set()
    p1 = [0,0]
    p2 = [0,0]
    for w in wire1:
        direction = w[0]
        distance = int(w[1:])

        for i in range(distance):
            if direction == 'U':
                p1[1] +=1
            elif direction == 'L':
                p1[0] -= 1
            elif direction == 'R':
                p1[0] += 1
            elif direction == 'D':
                p1[1] -= 1
            points1.add(tuple(p1))
    for w in wire2:
        direction = w[0]
        distance = int(w[1:])

        for i in range(distance):
            if direction == 'U':
                p2[1] +=1
            elif direction == 'L':
                p2[0] -= 1
            elif direction == 'R':
                p2[0] += 1
            elif direction == 'D':
                p2[1] -= 1
            points2.add(tuple(p2))
    intersection = points1.intersection(points2)
    mindist = 2**32-1
    for inter in intersection:
        if abs(inter[0]) + abs(inter[1]) < mindist:
            mindist = abs(inter[0]) + abs(inter[1])
    return mindist

def partTwo(f):
    wires = f.read().strip().split('\n')
    wire1 = wires[0].split(',')
    wire2 = wires[1].split(',')
    points1 = set()
    points2 = set()

    points1_dist = dict()
    points2_dist = dict()
    p1 = [0,0]
    p2 = [0,0]

    steps = 0
    for w in wire1:
        direction = w[0]
        distance = int(w[1:])

        for i in range(distance):
            steps += 1
            if direction == 'U':
                p1[1] +=1
            elif direction == 'L':
                p1[0] -= 1
            elif direction == 'R':
                p1[0] += 1
            elif direction == 'D':
                p1[1] -= 1
            points1.add(tuple(p1))
            if tuple(p1) not in points1_dist:
                points1_dist[tuple(p1)] = steps
    steps = 0
    for w in wire2:
        direction = w[0]
        distance = int(w[1:])

        for i in range(distance):
            steps += 1
            if direction == 'U':
                p2[1] +=1
            elif direction == 'L':
                p2[0] -= 1
            elif direction == 'R':
                p2[0] += 1
            elif direction == 'D':
                p2[1] -= 1
            points2.add(tuple(p2))
            if tuple(p2) not in points2_dist:
                points2_dist[tuple(p2)] = steps
    intersection = points1.intersection(points2)
    minDelay = float('inf')
    for inter in intersection:
        if points1_dist[inter] + points2_dist[inter] < minDelay:
            minDelay = points1_dist[inter] + points2_dist[inter]
    return minDelay


if __name__ == '__main__':
    with open("3.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")