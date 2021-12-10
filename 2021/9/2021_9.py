from timeit import default_timer as timer
from datetime import timedelta
from collections import deque

def inBounds(i, j, h, w):
    if i < 0 or j < 0 or i >= h or j >= w:
        return False
    return True


def partOne(f):
    data = [line.strip() for line in f.read().split()]
    risk = 0
    height = len(data)
    width = len(data[0])
    for i in range(len(data)):
        for j in range(len(data[i])):

            check = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

            isLow = True
            for p in check:
                if inBounds(*p, height, width):
                    if int(data[p[0]][p[1]]) <= int(data[i][j]):
                        isLow = False
            if isLow:
                risk += int(data[i][j]) + 1
    return risk

#--------------------------------------------------#
def findBasin(data, i, j):
    queue = deque()
    queue.append((i,j))
    basinPoints = set()
    count = 0
    while len(queue) > 0:
        # find new points
        x,y = queue.popleft()
        new_points = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for p1,p2 in new_points:
            if inBounds(p1, p2, len(data), len(data[x])) and (p1, p2) not in basinPoints and data[p1][p2] != '9':
                queue.append((p1,p2))

        basinPoints.add((x,y))
        # print(queue)
        # print(basinPoints)
        count += 1
        # if count == 2:
        #     break
    return basinPoints



def partTwo(f):
    data = [line.strip() for line in f.read().split()]
    basin_list = []
    visited = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i,j) not in visited and data[i][j] != '9':
                basin = findBasin(data, i, j)
                for point in basin:
                    visited.add(point)
                basin_list.append(basin)
    basin_list.sort(key=len)
    return len(basin_list[-1])*len(basin_list[-2])*len(basin_list[-3])


if __name__ == '__main__':
    with open('9.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
