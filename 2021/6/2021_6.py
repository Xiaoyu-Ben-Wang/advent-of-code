from timeit import default_timer as timer
from datetime import timedelta


class Fish:
    def __init__(self, age: int) -> None:
        self.age = age
        self.cycle=7
    def nextDay(self):
        if self.age == 0:
            self.age = self.cycle - 1
            return Fish(self.age+2)
        else:
            self.age -= 1
            return None


def partOne(f):
    fishies = set(Fish(int(n)) for n in f.read().strip().split(','))

    for _ in range(80):
        new_spawn = set()
        for fish in fishies:
            new_fish = fish.nextDay()
            if new_fish:
                new_spawn.add(new_fish)
        fishies = set.union(fishies, new_spawn)
    return len(fishies)


def partTwo(f):
    data = [int(n) for n in f.read().strip().split(',')]
    cycle = 7
    fishDict = dict()

    for n in data:
        fishDict[n] = fishDict.get(n, 0) + 1

    for _ in range(256):
        newFish = dict()
        for k, v in fishDict.items():
            if k ==0:
                newFish[cycle+1] = newFish.get(cycle+1, 0) + v
                newFish[cycle-1] = newFish.get(cycle-1, 0) + v
            else:
                newFish[k-1] = newFish.get(k-1, 0) + v

        fishDict = newFish
    return sum(fishDict.values())




if __name__ == '__main__':
    with open('6.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
