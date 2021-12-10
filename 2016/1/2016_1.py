from timeit import default_timer as timer


def partOne(f):
    X = 0
    Y = 0
    facing = 90
    directions = f.read().strip().split(', ')
    for d in directions:
        if d[0] == 'L':
            facing += 90
        elif d[0] == 'R':
            facing -= 90
        facing %= 360

        if facing == 0:
            X += int(d[1:])
        elif facing == 90:
            Y += int(d[1:])
        elif facing == 180:
            X -= int(d[1:])
        elif facing == 270:
            Y -= int(d[1:])
    return abs(X)+abs(Y)


def partTwo(f):
    locations = {(0, 0)}
    X = 0
    Y = 0
    facing = 90
    directions = f.read().strip().split(', ')
    for d in directions:
        if d[0] == 'L':
            facing += 90
        elif d[0] == 'R':
            facing -= 90
        facing %= 360

        val = int(d[1:])
        for i in range(val):
            if facing == 0:
                X += 1
            elif facing == 90:
                Y += 1
            elif facing == 180:
                X -= 1
            elif facing == 270:
                Y -= 1
            if (X, Y) in locations:
                return abs(X)+abs(Y)
            locations.add((X, Y))


if __name__ == '__main__':
    with open('1.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 Answer: {ans} ({(end-start)*1000:.5f} ms)")

        f.seek(0)

        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 Answer: {ans} ({(end-start)*1000:.5f} ms)")
