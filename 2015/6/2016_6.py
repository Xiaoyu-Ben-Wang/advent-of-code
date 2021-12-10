from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    lights = [[-1 for i in range(1000)] for j in range(1000)]
    instructions = f.read().strip().split('\n')
    for ins in instructions:
        ins = ins.split()

        if ins[0] == 'toggle':
            coord1 = tuple(int(i) for i in ins[1].split(','))
            coord2 = tuple(int(i) for i in ins[3].split(','))

            for i in range(coord1[0], coord2[0]+1):
                for j in range(coord1[1], coord2[1]+1):
                    lights[i][j] = -lights[i][j]

        elif ins[1] == 'off':
            coord1 = tuple(int(i) for i in ins[2].split(','))
            coord2 = tuple(int(i) for i in ins[4].split(','))
            for i in range(coord1[0], coord2[0]+1):
                for j in range(coord1[1], coord2[1]+1):
                    lights[i][j] = -1
        elif ins[1] == 'on':
            coord1 = tuple(int(i) for i in ins[2].split(','))
            coord2 = tuple(int(i) for i in ins[4].split(','))
            for i in range(coord1[0], coord2[0]+1):
                for j in range(coord1[1], coord2[1]+1):
                    lights[i][j] = 1
    count = 0
    for i in range(1000):
        for j in range(1000):
            if lights[i][j] == 1:
                count += 1
    return count


def partTwo(f):
    lights = [[0 for i in range(1000)] for j in range(1000)]
    instructions = f.read().strip().split('\n')
    for ins in instructions:
        ins = ins.split()

        if ins[0] == 'toggle':
            coord1 = tuple(int(i) for i in ins[1].split(','))
            coord2 = tuple(int(i) for i in ins[3].split(','))

            for i in range(coord1[0], coord2[0]+1):
                for j in range(coord1[1], coord2[1]+1):
                    lights[i][j] += 2

        elif ins[1] == 'off':
            coord1 = tuple(int(i) for i in ins[2].split(','))
            coord2 = tuple(int(i) for i in ins[4].split(','))
            for i in range(coord1[0], coord2[0]+1):
                for j in range(coord1[1], coord2[1]+1):
                    if lights[i][j] != 0:
                        lights[i][j] -= 1
        elif ins[1] == 'on':
            coord1 = tuple(int(i) for i in ins[2].split(','))
            coord2 = tuple(int(i) for i in ins[4].split(','))
            for i in range(coord1[0], coord2[0]+1):
                for j in range(coord1[1], coord2[1]+1):
                    lights[i][j] += 1
    return sum(sum(row) for row in lights)


if __name__ == '__main__':
    with open("6.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
