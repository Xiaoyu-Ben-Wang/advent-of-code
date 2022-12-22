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


def inRange(point):
    MAX = 4000000

    return point[0] >= 0 and point[1] >= 0 and point[0] <= MAX and point[1] <= MAX


def getPointsOutsideRange(center, radius):
    result = set()
    dist = radius+1
    for i in range(dist+1):
        new_points = [
            ((center[0]+i, center[1]+dist-i)),
            ((center[0]+i, center[1]-(dist-i))),
            ((center[0]-i, center[1]+dist-i)),
            ((center[0]-i, center[1]-(dist-i))),
        ]
        for p in new_points:
            if inRange(p):
                result.add(p)

    return result


def partTwo(f: TextIOWrapper):
    locations = [line.strip() for line in f.readlines()]

    PATTERN = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

    sensorDistanceMap = dict()
    beacons = set()

    potential_spots = set()

    for location in tqdm(locations):
        sensX, sensY, beaconX, beaconY = [int(s) for s in re.findall(PATTERN, location)[0]]

        sensor = (sensX, sensY)
        beacon = (beaconX, beaconY)
        radius = getMhtnDist(sensor, beacon)
        beacons.add(beacon)
        sensorDistanceMap[sensor] = radius

        for point in getPointsOutsideRange(sensor, radius):
            if point in beacons:
                continue
            if not inRange(point):
                continue
            valid = True
            for s, r in sensorDistanceMap.items():
                if getMhtnDist(point, s) <= r:
                    valid = False
            if valid:
                potential_spots.add(point)

    ans = []
    for spot in tqdm(potential_spots):
        if spot in beacons:
            continue
        if not inRange(spot):
            continue

        valid = True
        for sensor, radius in sensorDistanceMap.items():
            if getMhtnDist(spot, sensor) <= radius:
                valid = False

        if valid:
            ans.append(spot)

    spot = ans[0]
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
