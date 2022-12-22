from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    inp = int(f.read().strip())
    n = 1
    x = 0
    y = 0
    i = 1
    j = 1
    while True:
        if i == j:
            if i % 2 != 0:
                for k in range(i):
                    x += 1
                    n += 1
                    if n == inp:
                        return abs(x)+abs(y)
            else:
                for k in range(i):
                    x -= 1
                    n += 1
                    if n == inp:
                        return abs(x)+abs(y)
            i += 1
        else:
            if j % 2 != 0:
                for k in range(j):
                    y += 1
                    n +=1
                    if n == inp:
                        return abs(x)+abs(y)
            else:
                for k in range(j):
                    y -= 1
                    n += 1
                    if n == inp:
                        return abs(x)+abs(y)

            j += 1


class Direction:
    R = (1, 0)
    U = (0, 1)
    L = (-1, 0)
    D = (0, -1)

    order = [R, U, L, D]



def partTwo(f):
    inp = int(f.read().strip())
    numbers = dict()
    numbers[(0, 0)] = 1
    # order = right 1, up 1, left 2, down 2, right 3, up 3, left 4
    import time
    position = [0, 0]
    step_size = 1
    while True:
        for direction in Direction.order:
            for _ in range(step_size):
                position = [position[0] + direction[0], position[1] + direction[1]]

                surroundings = [
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0),
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1),
                ]
                val = 0
                for offset in surroundings:
                    s_point = (position[0] + offset[0], position[1] + offset[1])

                    val += numbers.get(s_point, 0)
                numbers[tuple(position)] = val

                if val > inp:
                    return val
            if direction == Direction.U or direction == Direction.D:
                step_size += 1








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