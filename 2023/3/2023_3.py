from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import re


def partOne(f: TextIOWrapper):
    matrix = list(line.strip() for line in f.readlines())

    def check(row, col):
        row = max(min(row, len(matrix)-1), 0)
        col = max(min(col, len(matrix[row])-1), 0)
        return matrix[row][col] == '.' or matrix[row][col].isdigit()

    def checkAround(row, start, end):
        inadjacent = True
        inadjacent = inadjacent and check(row, start-1)
        inadjacent = inadjacent and check(row, end)
        for i in range(start-1, end+1):
            inadjacent = inadjacent and check(row-1, i)
            inadjacent = inadjacent and check(row+1, i)
        return not inadjacent

    ans = 0
    for row in range(len(matrix)):
        re_matches = re.finditer(r'(\d+)', matrix[row])
        for match in re_matches:
            start, end = match.span()
            if checkAround(row, start, end):
                ans += int(match.group())

    return ans


def partTwo(f: TextIOWrapper):
    matrix = list(line.strip() for line in f.readlines())
    gears = {}

    def check(row, col):
        row = max(min(row, len(matrix)-1), 0)
        col = max(min(col, len(matrix[row])-1), 0)
        return matrix[row][col] == '*'

    def checkAround(row, start, end):
        gear = None
        if check(row, start-1):
            gear = (row, start-1)
        if check(row, end):
            gear = (row, end)

        for i in range(start-1, end+1):
            if check(row-1, i):
                gear = (row-1, i)
            if check(row+1, i):
                gear = (row+1, i)

        return gear

    ans = 0
    for row in range(len(matrix)):
        re_matches = re.finditer(r'(\d+)', matrix[row])
        for match in re_matches:
            start, end = match.span()
            gear = checkAround(row, start, end)
            if gear:
                gears[gear] = gears.get(gear, []) + [match.group()]
    for pair in gears.values():
        if len(pair) == 2:
            ans += int(pair[0])*int(pair[1])

    return ans


if __name__ == '__main__':
    with open('2023_3.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
