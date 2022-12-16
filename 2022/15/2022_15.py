import re
from datetime import timedelta
from io import TextIOWrapper
from timeit import default_timer as timer
from tqdm import tqdm


def getMhtnDist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1-x2)+abs(y1-y2)


def mergeIntervals(intervals):
    index = 0
    while index < len(intervals)-1:
        if intervals[index][1] >= intervals[index+1][0]:
            intervals[index] = (intervals[index][0], max(intervals[index][1], intervals[index+1][1]))
            intervals.pop(index+1)
        else:
            index += 1
    return intervals


def partOne(f: TextIOWrapper):
    locations = [line.strip() for line in f.readlines()]

    PATTERN = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

    sensorDistances = dict()
    beacons = set()

    for location in locations:
        sensX, sensY, beaconX, beaconY = [int(s) for s in re.findall(PATTERN, location)[0]]

        sensorDistances[(sensX, sensY)] = getMhtnDist((sensX, sensY), (beaconX, beaconY))
        beacons.add((beaconX, beaconY))

    ROW_Y = 2000000
    intervals = []
    for sensor, distance in sensorDistances.items():
        x, y = sensor
        vertical_diff = abs(ROW_Y-y)
        if vertical_diff > distance:
            continue
        room = distance-vertical_diff

        intervals.append((x-room, x+room))
    intervals.sort()
    total = 0
    for interval in mergeIntervals(intervals):
        total += interval[1]-interval[0]
        if interval[0]*interval[1] <= 0:
            total += 1

        counted_beacons = set()
        for beacon in beacons:
            x, y = beacon
            if y == ROW_Y and x >= interval[0] and x <= interval[1]:

                counted_beacons.add(beacon)
        total -= len(counted_beacons)
        for b in counted_beacons:
            beacons.remove(b)
    return total


def inRange(n):
    return n >= 0 and n <= 4000000


def partTwo(f: TextIOWrapper):
    locations = [line.strip() for line in f.readlines()]

    PATTERN = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

    sensorDistances = dict()
    beacons = set()

    potential_spots = set()

    for location in tqdm(locations):
        sensX, sensY, beaconX, beaconY = [int(s) for s in re.findall(PATTERN, location)[0]]

        dist = getMhtnDist((sensX, sensY), (beaconX, beaconY))
        sensorDistances[(sensX, sensY)] = dist
        beacons.add((beaconX, beaconY))

        x, y = sensX, sensY
        for xdiff in tqdm(range(dist+2)):
            ydiff = dist+1-x
            spots = [
                (x+xdiff, y+ydiff),
                (x+xdiff, y-ydiff),
                (x-xdiff, y+ydiff),
                (x-xdiff, y-ydiff),
            ]
            for spot in spots:
                if not inRange(spot[0]) or not inRange(spot[1]):
                    continue

                add = True
                for sensor, dist in sensorDistances.items():
                    if getMhtnDist(spot, sensor) <= dist:
                        add = False
                        break
                if add:
                    potential_spots.add(spot)
    for spot in tqdm(potential_spots):
        if not inRange(spot[0]) or not inRange(spot[1]):
            continue
        found = True
        for sensor, dist in sensorDistances.items():
            if spot not in beacons and getMhtnDist(spot, sensor) <= dist:
                found = False
                break
        if found:
            return spot[0]*4000000+spot[1]


if __name__ == '__main__':
    with open('2022_15.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
