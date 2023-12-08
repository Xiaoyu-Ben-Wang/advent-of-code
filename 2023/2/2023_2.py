from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import re


def partOne(f: TextIOWrapper):

    ans = 0
    for line in f.readlines():
        game_id = int(re.findall(r'Game (\d+)', line)[0])
        valid = True
        for handfull in line.split(';'):
            values = re.findall(r'(\d+) (red|green|blue)', handfull)
            red = 0
            blue = 0
            green = 0
            for data in values:
                if data[1] == 'red':
                    red += int(data[0])
                if data[1] == 'blue':
                    blue += int(data[0])
                if data[1] == 'green':
                    green += int(data[0])
            if red > 12 or green > 13 or blue > 14:
                valid = False
        if valid:
            ans += game_id

    return ans


def partTwo(f: TextIOWrapper):

    power = 0
    for line in f.readlines():
        game_id = int(re.findall(r'Game (\d+)', line)[0])
        red = 0
        blue = 0
        green = 0
        for handfull in line.split(';'):
            values = re.findall(r'(\d+) (red|green|blue)', handfull)

            for data in values:
                if data[1] == 'red':
                    red = max(int(data[0]), red)
                if data[1] == 'blue':
                    blue = max(int(data[0]), blue)
                if data[1] == 'green':
                    green = max(int(data[0]), green)
        power += red * blue * green

    return power


if __name__ == '__main__':
    with open('2023_2.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
