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



def partTwo(f):
    pass


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