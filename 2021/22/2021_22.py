from timeit import default_timer as timer
from datetime import timedelta
from progress.bar import Bar
import re


class Cube:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.state = 0


def between(cube, low, high):
    return


def partOne(f):
    regex = r'^x=(-?\d*)\.\.(-?\d*),y=(-?\d*)\.\.(-?\d*),z=(-?\d*)\.\.(-?\d*)$'

    data = f.read().splitlines()
    for i, val in enumerate(data):
        state = val.split(' ')[0]
        coords = re.findall(regex, val.split(' ')[1])[0]
        data[i] = {
            'state': 1 if state == 'on' else 0,
            'minX': int(coords[0]),
            'maxX': int(coords[1]),
            'minY': int(coords[2]),
            'maxY': int(coords[3]),
            'minZ': int(coords[4]),
            'maxZ': int(coords[5]),
        }
    cubes = set()
    for x in range(-50, 51):
        for y in range(-50, 51):
            for z in range(-50, 51):
                cubes.add(Cube(x, y, z))

    bar = Bar('In Progress', max=len(data))
    for ins in data:
        changed = list(filter(lambda c: c.x <= ins['maxX'] and c.x >= ins['minX'], cubes))
        changed = list(filter(lambda c: c.y <= ins['maxY'] and c.y >= ins['minY'], changed))
        changed = list(filter(lambda c: c.z <= ins['maxZ'] and c.z >= ins['minZ'], changed))
        for cube in changed:
            cube.state = ins['state']
        bar.next()
    print()
    count = 0
    for cube in cubes:
        if cube.state == 1:
            count += 1
    return count


def partTwo(f):
    pass


if __name__ == '__main__':
    with open('22.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
