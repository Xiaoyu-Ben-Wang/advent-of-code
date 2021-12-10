from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    count = 0
    triangles = f.read().split('\n')
    for i in range(len(triangles)):
        t = [int(n) for n in triangles[i].split()]
        if t[0]+t[1] > t[2] and t[1]+t[2] > t[0] and t[0]+t[2] > t[1]:
            count += 1
    return count


def partTwo(f):
    count = 0
    triangles = f.read().split('\n')
    for i in range(len(triangles)):
        triangles[i] = [int(n) for n in triangles[i].split()]
    for i in range(0, len(triangles), 3):
        sub_tri = [[triangles[i][j], triangles[i+1][j], triangles[i+2][j]] for j in range(3)]
        for t in sub_tri:
            if t[0]+t[1] > t[2] and t[1]+t[2] > t[0] and t[0]+t[2] > t[1]:
                count += 1
    return count


if __name__ == '__main__':
    with open('3.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
