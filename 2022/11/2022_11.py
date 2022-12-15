from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import re


class Item:
    def __init__(self, initial_val: int, divisors: list[int]):
        self.remainders = dict()
        for d in divisors:
            self.remainders[d] = initial_val % d

    def is_divisible(self, divisor: int):
        return self.remainders[divisor] % divisor == 0

    def transform(self, operation: str):
        for d in self.remainders:
            old = self.remainders[d]
            new = eval(operation)
            self.remainders[d] = new % d


class Monki1:
    def __init__(self, items: list[int], operation: str, test: int, true_dest: int, false_dest: int):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.inspections = 0

    def take_turn(self):
        results = []
        for i in range(len(self.items)):
            old = self.items[i]
            new = eval(self.operation.replace('old', str(old)))
            new = new // 3
            if new % self.test == 0:
                results.append((new, self.true_dest))
            else:
                results.append((new, self.false_dest))
            self.inspections += 1
        self.items = []
        return results

    def add_item(self, val):
        self.items.append(val)

class Monki2:
    def __init__(self, items: list[int], operation: str, test: int, true_dest: int, false_dest: int, divisors: list[int]):
        self.items = [Item(it, divisors) for it in items]
        self.operation = operation
        self.test = test
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.inspections = 0

    def take_turn(self):
        results = []
        for i in range(len(self.items)):
            self.items[i].transform(self.operation)
            if self.items[i].is_divisible(self.test):
                results.append((self.items[i], self.true_dest))
            else:
                results.append((self.items[i], self.false_dest))
            self.inspections += 1
        self.items = []
        return results

    def add_item(self, val):
        self.items.append(val)


REGEX = r'Monkey (\d+):\s+Starting items\: (.*)\s+Operation: new = (.*)\s+Test: divisible by (\d+)\s+If true: throw to monkey (\d+)\s+If false: throw to monkey (\d+)'


def partOne(f: TextIOWrapper):
    monkis = dict()

    info = f.read()
    matches = re.findall(REGEX, info)
    divisors = []
    for match in matches:
        num, items, operation, test, true_dest, false_dest = match
        num = int(num)
        items = [int(n) for n in items.split(', ')]
        test = int(test)
        divisors.append(test)
        true_dest = int(true_dest)
        false_dest = int(false_dest)

        monki = Monki1(items, operation, test, true_dest, false_dest)
        monkis[num] = monki

    round_count = 0
    while round_count < 20:
        for k in sorted(monkis.keys()):
            results = monkis[k].take_turn()
            for r in results:
                item, dest = r
                monkis[dest].add_item(item)
        round_count += 1

    return sorted(m.inspections for m in monkis.values())[-1]*sorted(m.inspections for m in monkis.values())[-2]


def partTwo(f: TextIOWrapper):
    monkis = dict()

    info = f.read()
    matches = re.findall(REGEX, info)
    divisors = []
    for match in matches:
        num, items, operation, test, true_dest, false_dest = match
        divisors.append(int(test))

    for match in matches:
        num, items, operation, test, true_dest, false_dest = match
        num = int(num)
        items = [int(n) for n in items.split(', ')]
        test = int(test)
        true_dest = int(true_dest)
        false_dest = int(false_dest)

        monki = Monki2(items, operation, test, true_dest, false_dest, divisors)
        monkis[num] = monki

    round_count = 0
    while round_count < 10000:
        for k in sorted(monkis.keys()):
            results = monkis[k].take_turn()
            for r in results:
                item, dest = r
                monkis[dest].add_item(item)
        round_count += 1
        print(f'{round_count}/10000', end='\r')

    return sorted(m.inspections for m in monkis.values())[-1]*sorted(m.inspections for m in monkis.values())[-2]


if __name__ == '__main__':
    with open('2022_11.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
