from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import time
import os


class Direction:
    N = 'N'
    S = 'S'
    E = 'E'
    W = 'W'


def getNextStep(point, direction):
    row, col = point
    if direction == Direction.N:
        return (row-1, col)
    elif direction == Direction.S:
        return (row+1, col)
    elif direction == Direction.W:
        return (row, col-1)
    elif direction == Direction.E:
        return (row, col+1)
    else:
        raise Exception


def getSurroudingPoints(point):
    row, col = point

    return [
        (row-1, col-1),
        (row-1, col),
        (row-1, col+1),
        (row+1, col-1),
        (row+1, col),
        (row+1, col+1),
        (row, col+1),
        (row, col-1),
    ]


def getRelativePoints(point, direction):
    row, col = point
    if direction == Direction.N:
        return [
            (row-1, col-1),
            (row-1, col),
            (row-1, col+1),
        ]
    elif direction == Direction.S:
        return [
            (row+1, col-1),
            (row+1, col),
            (row+1, col+1),
        ]
    elif direction == Direction.W:
        return [
            (row-1, col-1),
            (row, col-1),
            (row+1, col-1),
        ]
    elif direction == Direction.E:
        return [
            (row-1, col+1),
            (row, col+1),
            (row+1, col+1),
        ]
    else:
        raise Exception


def draw(positions):
    os.system('cls')
    offset = 5
    size = 20
    output = []
    for row in range(size):
        line = []
        for col in range(size):
            if (row-offset, col-offset) in positions:
                line.append('#')
            else:
                line.append('.')
        output.append(''.join(line))
    print('\n'.join(output))
    print(PROPOSAL_ORDER)
    print(f'size: {len(positions)}')
    time.sleep(2)


PROPOSAL_ORDER = [
    Direction.N,
    Direction.S,
    Direction.W,
    Direction.E
]


def cycleProposalOrder():
    PROPOSAL_ORDER.append(PROPOSAL_ORDER.pop(0))


class Elf:
    def __init__(self, position) -> None:
        self.position = position

    def get_next_proposed_step(self, existing_positions: set):
        # check if elfs around
        surrounding_positions = getSurroudingPoints(self.position)
        has_nearby_elf = False
        for p in surrounding_positions:
            if p in existing_positions:
                has_nearby_elf = True
        if not has_nearby_elf:
            return self.position

        for direction in PROPOSAL_ORDER:
            points = getRelativePoints(self.position, direction)
            elf_in_that_direction = False
            for p in points:
                if p in existing_positions:
                    elf_in_that_direction = True

            if not elf_in_that_direction:

                return getNextStep(self.position, direction)
        return self.position


def partOne(f: TextIOWrapper):
    grid = [list(line) for line in f.read().splitlines()]

    elves = set()

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '#':
                elves.add(Elf((row, col)))

    for _ in range(10):
        x = input()
        current_positions = set([e.position for e in elves])
        draw(current_positions)
        elf_to_future_position = dict()
        proposed_position_counter = dict()
        for elf in elves:
            proposed_position = elf.get_next_proposed_step(current_positions)
            elf_to_future_position[elf] = proposed_position
            proposed_position_counter[proposed_position] = proposed_position_counter.get(proposed_position, 0) + 1

        elves.clear()
        for elf, future_pos in elf_to_future_position.items():
            if proposed_position_counter[future_pos] > 1:
                elves.add(elf)
            else:
                elf.position = future_pos
                elves.add(elf)
        cycleProposalOrder()
    draw(current_positions)
    row_range = (float('inf'), float('-inf'))
    col_range = (float('inf'), float('-inf'))

    for elf in elves:
        row, col = elf.position
        row_range = (min(row_range[0], row), max(row_range[1], row))
        col_range = (min(col_range[0], col), max(col_range[1], col))
    print(row_range)
    print(col_range)
    return (row_range[1] - row_range[0])*(col_range[1]-col_range[0]) - len(elves)


def partTwo(f: TextIOWrapper):
    pass


if __name__ == '__main__':
    with open('2022_23.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
