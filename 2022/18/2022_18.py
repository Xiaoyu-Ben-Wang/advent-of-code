from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    all_cubes = set([tuple(int(n) for n in line.split(',')) for line in f.read().splitlines()])

    exposed = 0

    for cube in all_cubes:
        potential_cubes = [
            (cube[0]+1, cube[1], cube[2]),
            (cube[0]-1, cube[1], cube[2]),
            (cube[0], cube[1]+1, cube[2]),
            (cube[0], cube[1]-1, cube[2]),
            (cube[0], cube[1], cube[2]+1),
            (cube[0], cube[1], cube[2]-1),
        ]

        for p_cube in potential_cubes:
            if p_cube not in all_cubes:
                exposed += 1
    return exposed


def partTwo(f: TextIOWrapper):
    all_cubes = set([tuple(int(n) for n in line.split(',')) for line in f.read().splitlines()])

    max_x = 0
    max_y = 0
    max_z = 0

    for cube in all_cubes:
        max_x = max(cube[0], max_x)
        max_y = max(cube[1], max_y)
        max_z = max(cube[2], max_z)
    max_x += 2
    max_y += 2
    max_z += 2

    water = set()
    water.add((-1, -1, -1))

    def isWaterPosValid(drop):
        return (drop[0] >= -1 and drop[0] <= max_x and
                drop[1] >= -1 and drop[1] <= max_y and
                drop[2] >= -1 and drop[2] <= max_z)

    while True:
        changed = False
        new_water = set()
        for drop in water:
            potential_drops = [
                (drop[0]+1, drop[1], drop[2]),
                (drop[0]-1, drop[1], drop[2]),
                (drop[0], drop[1]+1, drop[2]),
                (drop[0], drop[1]-1, drop[2]),
                (drop[0], drop[1], drop[2]+1),
                (drop[0], drop[1], drop[2]-1),
            ]
            for p_drop in potential_drops:
                if p_drop not in water and p_drop not in all_cubes and isWaterPosValid(p_drop):
                    new_water.add(p_drop)
                    changed = True
        for new_drop in new_water:
            water.add(new_drop)

        if not changed:
            break

    exposed = 0
    for cube in all_cubes:
        potential_cubes = [
            (cube[0]+1, cube[1], cube[2]),
            (cube[0]-1, cube[1], cube[2]),
            (cube[0], cube[1]+1, cube[2]),
            (cube[0], cube[1]-1, cube[2]),
            (cube[0], cube[1], cube[2]+1),
            (cube[0], cube[1], cube[2]-1),
        ]
        for p_cube in potential_cubes:
            if p_cube not in all_cubes and p_cube in water:
                exposed += 1
    return exposed


if __name__ == '__main__':
    with open('2022_18.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
