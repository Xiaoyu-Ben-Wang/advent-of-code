from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import re


def partOne(f: TextIOWrapper):
    ans = 0
    for match in re.findall(r'mul\((\d+),(\d+)\)', f.read()):
        ans += int(match[0])*int(match[1])
    return ans


def partTwo(f: TextIOWrapper):
    ans = 0
    enabled = True
    for match in re.findall(r'(?:mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))', f.read()):
        if match[2]:
            enabled = True
        if match[3]:
            enabled = False
        if (match[0] and match[1] and enabled):
            ans += int(match[0])*int(match[1])
    return ans


if __name__ == '__main__':
    with open('2024_3.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
