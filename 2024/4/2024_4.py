from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    matrix = [[letter for letter in line] for line in f.read().split('\n')]
    LETTERS = 'XMAS'
    DIRECTIONS = [
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (1, 0),
        (-1, 0),
        (-1, -1),
        (-1, 1)
    ]
    valid = set()

    def check(row, col, direction: tuple):
        r = row
        c = col
        possible_valid = []
        try:
            for letter in LETTERS:
                if r < 0 or c < 0:
                    return False
                if matrix[r][c] == letter:
                    possible_valid.append((r, c))
                    r += direction[0]
                    c += direction[1]
                else:
                    return False
        except IndexError:
            return False
        for tp in possible_valid:
            valid.add(tp)
        return True
    ans = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            for d in DIRECTIONS:
                if check(row, col, d):
                    ans += 1
    return ans


def partTwo(f: TextIOWrapper):
    matrix = [[letter for letter in line] for line in f.read().split('\n')]
    LETTERS = 'XMAS'
    DIRECTIONS = [
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (1, 0),
        (-1, 0),
        (-1, -1),
        (-1, 1)
    ]
    valid = set()

    def check(row, col, m_directions):
        if matrix[row][col] != 'A':
            return False
        if matrix[row+m_directions[0][0]][col+m_directions[0][1]] != 'M':
            return False
        if matrix[row+m_directions[1][0]][col+m_directions[1][1]] != 'M':
            return False
        if matrix[row-m_directions[0][0]][col-m_directions[0][1]] != 'S':
            return False
        if matrix[row-m_directions[1][0]][col-m_directions[1][1]] != 'S':
            return False
        return True
    ans = 0
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row])-1):
            if check(row, col, [(-1, -1), (-1, 1)]):
                ans += 1
            if check(row, col, [(-1, 1), (1, 1)]):
                ans += 1
            if check(row, col, [(1, -1), (1, 1)]):
                ans += 1
            if check(row, col, [(-1, -1), (1, -1)]):
                ans += 1
    return ans


if __name__ == '__main__':
    with open('2024_4.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
