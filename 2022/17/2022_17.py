from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
from colorama import Back, Style
from tqdm import tqdm


class Rocks:
    DASH = {
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
    }

    PLUS = {
        (0, 1),
        (1, 0),
        (1, 1),
        (2, 1),
        (1, 2),
    }

    REVL = {
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2),
    }

    LINE = {
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
    }

    SQUARE = {
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
    }

    order = [DASH, PLUS, REVL, LINE, SQUARE]

    @staticmethod
    def getRock(start, rock):
        new_rock = set()
        for point in rock:
            new_rock.add((point[0] + start[0], point[1]+start[1]))
        return new_rock


class Gust:
    L = '<'
    R = '>'


def isValidNext(rock: set, locations: set, width: int):
    for point in rock:
        if point in locations:
            return False
        if point[0] >= width or point[0] < 0:
            return False
        if point[1] < 0:
            return False
    return True


def partOne(f: TextIOWrapper):
    gusts = list(f.read().strip())

    rock_index = 0
    gust_index = 0
    fallen = 0

    WIDTH = 7
    START = [2, 3]
    lowest = 0

    locations = set()

    for _ in range(2022):
        # rock spawn
        new_rock = Rocks.getRock(START, Rocks.order[rock_index])
        rock_index = (rock_index + 1) % len(Rocks.order)
        while True:

            # try push by gust
            gust = gusts[gust_index]

            gust_index = (gust_index + 1) % len(gusts)
            next_rock = set()

            if gust == Gust.L:
                for point in new_rock:
                    next_rock.add((point[0]-1, point[1]))
            elif gust == Gust.R:
                for point in new_rock:
                    next_rock.add((point[0]+1, point[1]))
            else:
                raise Exception("???")

            if isValidNext(next_rock, locations, WIDTH):
                new_rock = next_rock

            next_rock = set()
            for point in new_rock:
                next_rock.add((point[0], point[1]-1))
            if isValidNext(next_rock, locations, WIDTH):
                new_rock = next_rock
            else:
                for point in new_rock:
                    if point[1]+1 > lowest:
                        lowest = point[1]+1
                        START = [2, lowest+3]
                    locations.add(point)
                fallen += 1
                break

    return lowest


def partTwo(f: TextIOWrapper):
    gusts = list(f.read().strip())
    data = [None for _ in range(100001)]
    heights = [None for _ in range(100001)]
    data[0] = 0
    heights[0] = 0

    rock_index = 0
    gust_index = 0
    fallen = 0

    WIDTH = 7
    START = [2, 3]
    lowest = 0

    locations = set()

    for _ in tqdm(range(100000)):
        # rock spawn
        new_rock = Rocks.getRock(START, Rocks.order[rock_index])
        rock_index = (rock_index + 1) % len(Rocks.order)
        while True:

            # try push by gust
            gust = gusts[gust_index]

            gust_index = (gust_index + 1) % len(gusts)
            next_rock = set()

            if gust == Gust.L:
                for point in new_rock:
                    next_rock.add((point[0]-1, point[1]))
            elif gust == Gust.R:
                for point in new_rock:
                    next_rock.add((point[0]+1, point[1]))
            else:
                raise Exception("???")

            if isValidNext(next_rock, locations, WIDTH):
                new_rock = next_rock

            next_rock = set()
            for point in new_rock:
                next_rock.add((point[0], point[1]-1))
            if isValidNext(next_rock, locations, WIDTH):
                new_rock = next_rock
            else:
                new_lowest = lowest
                for point in new_rock:
                    if point[1]+1 > new_lowest:
                        new_lowest = point[1]+1
                        START = [2, new_lowest+3]
                    locations.add(point)
                fallen += 1
                data[fallen] = new_lowest-lowest
                heights[fallen] = new_lowest

                lowest = new_lowest
                break
    cycle_start = 0
    cycle_size = 0
    cycle_values = []
    for size in tqdm(range(10, len(data)//2+1)):
        should_break = False
        for index in range(0, len(data)-size, size):
            try:
                if data[index: index+size] == data[index+size:index+size+size]:
                    cycle_start = index
                    cycle_size = size
                    cycle_values = data[index: index+size]
                    should_break = True
                    break
            except IndexError:
                pass
        if should_break:
            break

    return heights[cycle_start] + ((1000000000000-cycle_start) // cycle_size) * sum(cycle_values) + sum(cycle_values[:1000000000000 % cycle_size+1])


if __name__ == '__main__':
    with open('2022_17.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
