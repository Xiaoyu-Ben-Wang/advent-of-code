from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import re


def partOne(f: TextIOWrapper):
    PATTERN = r'((?:\w+-)+)(\d+)\[(\w+)\]'
    rooms = [line.strip() for line in f.readlines()]
    total = 0
    for room in rooms:
        info, sector_id, checksum = re.findall(PATTERN, room)[0]
        counter = dict()
        for c in info:
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                counter[c] = counter.get(c, 0)+1

        sorted_order = sorted(counter.keys(), key= lambda item: (-counter[item], ord(item)))
        if ''.join(sorted_order[:5])== checksum:
            total += int(sector_id)
    return total

        
def shift(c, dist):
    if c == ' ':
        return c
    return chr((ord(c)-ord('a') + dist)% 26 + ord('a'))


def partTwo(f: TextIOWrapper):
    PATTERN = r'((?:\w+-)+)(\d+)\[(\w+)\]'
    rooms = [line.strip() for line in f.readlines()]
    real_rooms = []
    for room in rooms:
        info, sector_id, checksum = re.findall(PATTERN, room)[0]
        counter = dict()
        for c in info:
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                counter[c] = counter.get(c, 0)+1

        sorted_order = sorted(counter.keys(), key= lambda item: (-counter[item], ord(item)))
        if ''.join(sorted_order[:5])== checksum:
            info = info.replace('-', ' ').strip()
            name = ''.join(shift(c, int(sector_id)) for c in info)
            if 'northpole' in name:
                return sector_id


if __name__ == '__main__':
    with open('2016_4.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')