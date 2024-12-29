from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    matrix = [list(line) for line in f.read().split()]
    coords = [0, 0]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '^':
                coords = [row, col]
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    dir_index = 0
    while True:
        matrix[coords[0]][coords[1]] = 'X'
        direction = directions[dir_index]
        next_loc = [coords[0]+direction[0], coords[1]+direction[1]]
        if next_loc[0] < 0 or next_loc[0] >= len(matrix) or next_loc[1] < 0 or next_loc[1] >= len(matrix[0]):
            break
        if matrix[next_loc[0]][next_loc[1]] == '#':
            dir_index = (dir_index + 1) % len(directions)
        else:
            coords = next_loc

    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'X':
                count += 1

    return count


def isLoop(matrix, start, block):
    coords_slow = list(start)
    coords_fast = list(start)
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    dir_index_fast = 0
    dir_index_slow = 0
    while True:
        while True:
            # advance fast pointer
            direction = directions[dir_index_fast]
            next_loc = [coords_fast[0]+direction[0], coords_fast[1]+direction[1]]
            if next_loc[0] < 0 or next_loc[0] >= len(matrix) or next_loc[1] < 0 or next_loc[1] >= len(matrix[0]):
                return False
            if matrix[next_loc[0]][next_loc[1]] == '#' or (next_loc[0] == block[0] and next_loc[1] == block[1]):
                dir_index_fast = (dir_index_fast + 1) % len(directions)
                continue
            else:
                coords_fast = next_loc
                break
        if coords_fast[0] == coords_slow[0] and coords_fast[1] == coords_slow[1] and dir_index_fast == dir_index_slow:
            return True

        while True:
            # advance fast again
            direction = directions[dir_index_fast]
            next_loc = [coords_fast[0]+direction[0], coords_fast[1]+direction[1]]
            if next_loc[0] < 0 or next_loc[0] >= len(matrix) or next_loc[1] < 0 or next_loc[1] >= len(matrix[0]):
                return False
            if matrix[next_loc[0]][next_loc[1]] == '#' or (next_loc[0] == block[0] and next_loc[1] == block[1]):
                dir_index_fast = (dir_index_fast + 1) % len(directions)
                continue
            else:
                coords_fast = next_loc
                break

        if coords_fast[0] == coords_slow[0] and coords_fast[1] == coords_slow[1] and dir_index_fast == dir_index_slow:
            return True

        while True:
            # advance slow
            direction = directions[dir_index_slow]
            next_loc = [coords_slow[0]+direction[0], coords_slow[1]+direction[1]]

            if matrix[next_loc[0]][next_loc[1]] == '#' or (next_loc[0] == block[0] and next_loc[1] == block[1]):
                dir_index_slow = (dir_index_slow + 1) % len(directions)
                continue
            else:
                coords_slow = next_loc
                break


def partTwo(f: TextIOWrapper):

    matrix = [list(line) for line in f.read().split()]
    coords = [0, 0]
    start = None
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '^':
                coords = [row, col]
                start = (row, col)
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    dir_index = 0
    visited = set()
    while True:
        visited.add((coords[0], coords[1]))
        direction = directions[dir_index]
        next_loc = [coords[0]+direction[0], coords[1]+direction[1]]
        if next_loc[0] < 0 or next_loc[0] >= len(matrix) or next_loc[1] < 0 or next_loc[1] >= len(matrix[0]):
            break
        if matrix[next_loc[0]][next_loc[1]] == '#':
            dir_index = (dir_index + 1) % len(directions)
        else:
            coords = next_loc
    visited.remove(start)
    count = 0
    for blocker in visited:
        if isLoop(matrix, start, blocker):
            # matrix[blocker[0]][blocker[1]] = '+'
            count += 1
    # for line in matrix:
    #     print(''.join(line))
    return count


if __name__ == '__main__':
    with open('2024_6.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
