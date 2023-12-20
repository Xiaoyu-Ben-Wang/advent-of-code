from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import math


def partOne(f: TextIOWrapper):
    times, distances = [
        [int(n) for n in line.strip().split()[1:]] for line in f.readlines()
    ]
    ans = 1
    for i in range(len(times)):
        race_time = times[i]
        race_dist = distances[i]
        wins = 0
        for s in range(race_time + 1):
            if s * (race_time - s) > race_dist:
                wins += 1
        ans = ans * wins
    return ans


def partTwo(f: TextIOWrapper):
    times, distances = [
        int(line.strip().replace(" ", "").split(":")[1]) for line in f.readlines()
    ]
    # d = -s^2+st
    ans1 = math.floor((-times - math.sqrt(times**2 - (4 * (distances)))) / (-2))
    ans2 = math.floor((-times + math.sqrt(times**2 - (4 * (distances)))) / (-2))
    return math.floor(abs(ans1 - ans2))
    # return abs(ans - (times - ans))


if __name__ == "__main__":
    with open("2023_6.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
