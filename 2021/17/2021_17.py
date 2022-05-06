from timeit import default_timer as timer
from datetime import timedelta
import re


def cSum(n):
    return sum(n-i for i in range(n))


def partOne(f):
    data = f.read().strip()
    xMin, xMax, yMin, yMax = [int(n) for n in re.findall(r'^target area: x\=(.*)\.\.(.*), y\=(.*)\.\.(.*)$', data)[0]]
    return cSum(abs(yMin)-1)


def calcPath(pos, speedX, speedY, steps):
    points = set()
    points.add(pos)

    for _ in range(steps):
        pos = (pos[0] + speedX, pos[1] + speedY)
        points.add(pos)

        speedY -= 1
        if speedX > 0:
            speedX -= 1
        elif speedX < 0:
            speedX += 1
    return points


def hitTarget(x, y, rangeX, rangeY):
    return rangeX[0] <= x and rangeX[1] >= x and rangeY[0] <= y and rangeY[1] >= y


def partTwo(f):
    data = f.read().strip()
    xMin, xMax, yMin, yMax = [int(n) for n in re.findall(r'^target area: x\=(.*)\.\.(.*), y\=(.*)\.\.(.*)$', data)[0]]

    paths = 0
    for x in range(200):
        for y in range(-200, 200):
            STEPS = 350
            points = calcPath((0, 0), x, y, STEPS)
            hit = False
            for p in points:
                if hitTarget(p[0], p[1], (xMin, xMax), (yMin, yMax)):
                    paths += 1
                    break

    return paths


if __name__ == '__main__':
    with open('17.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
