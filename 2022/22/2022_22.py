import os
import re
import time
from datetime import timedelta
from io import TextIOWrapper
from timeit import default_timer as timer

import pygame
from colorama import Back, Style


class Direction:
    R = 0
    D = 1
    L = 2
    U = 3

    cycle = [R, D, L, U]


class Elf:
    def __init__(self) -> None:
        self.direction = Direction.R
        self.row = 0
        self.col = 0

    def getNextStep(self):
        if self.direction == Direction.R:
            return self.row, self.col+1
        elif self.direction == Direction.L:
            return self.row, self.col-1
        elif self.direction == Direction.U:
            return self.row-1, self.col
        elif self.direction == Direction.D:
            return self.row+1, self.col
        raise Exception

    def takeNextStep(self):
        if self.direction == Direction.R:
            self.col += 1
            return
        elif self.direction == Direction.L:
            self.col -= 1
            return
        elif self.direction == Direction.U:
            self.row -= 1
            return
        elif self.direction == Direction.D:
            self.row += 1
            return
        raise Exception

    def __repr__(self) -> str:
        return str(vars(self))


def findStart(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '.':
                return row, col
    raise Exception('Start not found')


def partOne(f: TextIOWrapper):
    pygame.init()
    canvas = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("Falling Sand")

    PATTERN = r'(\d+|\w)'
    PATH_SYMBOLS = ['>', '<', 'V', '^']

    grid, instructions = f.read().split('\n\n')
    grid = [list(line) for line in grid.splitlines()]
    max_length = max([len(line) for line in grid])
    for row in range(len(grid)):
        if len(grid[row]) != max_length:
            grid[row].extend([' ']*(max_length-len(grid[row])))
    instructions = [int(step) if step.isdigit() else step for step in re.findall(PATTERN, instructions)]

    elf = Elf()
    elf.row, elf.col = findStart(grid)

    def findWraparound(elf: Elf):
        row, col = elf.row, elf.col
        try:
            if elf.direction == Direction.R:
                while col > 0 and grid[row][col-1] != ' ':
                    col -= 1
                return row, col
            elif elf.direction == Direction.U:
                while grid[row+1][col] != ' ':
                    row += 1
                return row, col
            elif elf.direction == Direction.D:
                while row > 0 and grid[row-1][col] != ' ':
                    row -= 1
                return row, col
            elif elf.direction == Direction.L:
                while grid[row][col+1] != ' ':
                    col += 1
                return row, col
        except IndexError:
            return row, col
        raise Exception

    def move(elf: Elf, steps):
        for s in range(steps):

            next_row, next_col = elf.getNextStep()
            try:
                if grid[next_row][next_col] == '#':
                    break
                elif grid[next_row][next_col] == ' ':
                    next_row, next_col = findWraparound(elf)
                    if grid[next_row][next_col] == '#':
                        break
                    elf.row = next_row
                    elf.col = next_col
                else:
                    elf.takeNextStep()
            except IndexError:
                next_row, next_col = findWraparound(elf)
                elf.row = next_row
                elf.col = next_col
                if grid[next_row][next_col] == '#':
                    break
            if elf.direction == Direction.R:
                grid[elf.row][elf.col] = '>'
            elif elf.direction == Direction.L:
                grid[elf.row][elf.col] = '<'
            elif elf.direction == Direction.U:
                grid[elf.row][elf.col] = '^'
            elif elf.direction == Direction.D:
                grid[elf.row][elf.col] = 'V'
            draw(pygame, canvas, pygame.display)

    def printGraph():
        time.sleep(1)
        os.system('cls')
        for row in range(len(grid)):
            line = []
            for col in range(len(grid[row])):
                if elf.row == row and elf.col == col:
                    if elf.direction == Direction.R:
                        line.append(Back.GREEN+'>'+Style.RESET_ALL)
                    elif elf.direction == Direction.L:
                        line.append(Back.GREEN+'<'+Style.RESET_ALL)
                    elif elf.direction == Direction.U:
                        line.append(Back.GREEN+'^'+Style.RESET_ALL)
                    elif elf.direction == Direction.D:
                        line.append(Back.GREEN+'V'+Style.RESET_ALL)
                else:
                    char = grid[row][col]
                    if char == '#':
                        line.append(Back.RED+char+Style.RESET_ALL)
                    else:
                        line.append(grid[row][col])
            print(''.join(line))

    def draw(pygame, canvas, display):
        SCALE = 4
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                y, x = row, col
                if elf.row == row and elf.col == col:

                    pygame.draw.rect(canvas, (116, 235, 52), pygame.Rect(x*SCALE, y*SCALE, SCALE, SCALE))
                else:
                    char = grid[row][col]
                    if char in PATH_SYMBOLS:
                        pygame.draw.rect(canvas, (229, 235, 52), pygame.Rect(x*SCALE, y*SCALE, SCALE, SCALE))
                    elif char == '.':
                        pygame.draw.rect(canvas, (209, 209, 209), pygame.Rect(x*SCALE, y*SCALE, SCALE, SCALE))
                    elif char == '#':
                        pygame.draw.rect(canvas, (255, 71, 71), pygame.Rect(x*SCALE, y*SCALE, SCALE, SCALE))
        display.update()

    for ins in instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit("Quit Pygame")

        if type(ins) == int:
            move(elf, ins)
        else:
            prev_direction = elf.direction
            if ins == 'R':
                elf.direction = Direction.cycle[(Direction.cycle.index(prev_direction)+1) % len(Direction.cycle)]
            elif ins == 'L':
                elf.direction = Direction.cycle[(Direction.cycle.index(prev_direction)-1) % len(Direction.cycle)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1000 * (elf.row+1) + 4 * (elf.col + 1) + elf.direction


def partTwo(f: TextIOWrapper):
    pass


if __name__ == '__main__':
    with open('2022_22.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
