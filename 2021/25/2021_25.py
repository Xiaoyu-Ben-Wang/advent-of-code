from os import truncate
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    grid = [list(line) for line in f.read().splitlines()]
    step = 0
    # printgrid(grid)
    while True:
        changed = False
        updates = dict()
        # move east
        for i, _ in enumerate(grid):
            for j, val in enumerate(grid[i]):
                check = grid[i][(j+1)%len(grid[i])]
                if val == '>' and check == '.':
                    updates[(i, (j+1) % len(grid[i]))] = val
                    updates[(i,j)] = '.'
                    changed = True
        for (x,y), val in updates.items():
            grid[x][y] = val
        updates.clear()

        # move south
        for i, _ in enumerate(grid):
            for j, val in enumerate(grid[i]):
                check = grid[(i+1)%len(grid)][j]
                if val == 'v' and check == '.':
                    updates[((i+1) % len(grid), j)] = val
                    updates[(i, j)] = '.'
                    changed = True

        for (x, y), val in updates.items():
            grid[x][y] = val

        step += 1
        if not changed:
            break
    return step



if __name__ == '__main__':
    with open('25.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')