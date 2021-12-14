from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    points, instruction = f.read().split('\n\n')
    points = points.split()

    for i, p in enumerate(points):
        points[i] = tuple([int(n) for n in p.strip().split(',')])
    points = set(points)
    instruction = instruction.split('\n')
    firstIns = instruction[0].split(' ')[-1].split('=')
    firstIns[1] = int(firstIns[1])
    newpoints = set()
    if firstIns[0] == 'x':
        for x, y in points:
            if x > firstIns[1]:
                x = 2*firstIns[1]-x
            newpoints.add((x, y))

    elif firstIns[0] == 'y':
        for x, y in points:
            if y > firstIns[1]:
                y = 2*firstIns[1]-y
            newpoints.add((x, y))
    return len(newpoints)


def partTwo(f):
    points, instruction = f.read().split('\n\n')
    points = points.split()

    for i, p in enumerate(points):
        points[i] = tuple([int(n) for n in p.strip().split(',')])
    points = set(points)
    instruction = instruction.split('\n')
    for i, val in enumerate(instruction):
        line = val.split(' ')[-1].split('=')
        instruction[i] = (line[0], int(line[1]))

    for ins in instruction:
        newpoints = set()
        if ins[0] == 'x':
            for x, y in points:
                if x > ins[1]:
                    x = 2*ins[1]-x
                newpoints.add((x, y))

        elif ins[0] == 'y':
            for x, y in points:
                if y > ins[1]:
                    y = 2*ins[1]-y
                newpoints.add((x, y))
        points = newpoints

    display = [[' ' for _ in range(50)] for p in range(10)]
    for x, y in points:
        display[y][x] = '#'
    with open('Part2Result.txt', 'w+') as f:
        for line in display:
            f.write(''.join(line)+'\n')


if __name__ == '__main__':
    with open('13.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
