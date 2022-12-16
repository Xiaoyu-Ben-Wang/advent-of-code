from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


class Ship1:
    def __init__(self) -> None:
        self.X = 0
        self.Y = 0
        self.angle = 0

    def readInput(self, d):
        if d[0] == 'N':
            self.Y += int(d[1:])
        elif d[0] == 'S':
            self.Y -= int(d[1:])
        elif d[0] == 'E':
            self.X += int(d[1:])
        elif d[0] == 'W':
            self.X -= int(d[1:])
        elif d[0] == 'R':
            self.angle -= int(d[1:])
            self.angle %= 360
        elif d[0] == 'L':
            self.angle += int(d[1:])
            self.angle %= 360
        elif d[0] == 'F':
            if self.angle == 0:
                self.X += int(d[1:])
            elif self.angle == 90:
                self.Y += int(d[1:])
            elif self.angle == 180:
                self.X -= int(d[1:])
            elif self.angle == 270:
                self.Y -= int(d[1:])

    def getDist(self):
        return sum([abs(self.X), abs(self.Y)])

class Ship1:
    def __init__(self) -> None:
        self.X = 0
        self.Y = 0
        self.angle = 0

    def readInput(self, d):
        if d[0] == 'N':
            self.Y += int(d[1:])
        elif d[0] == 'S':
            self.Y -= int(d[1:])
        elif d[0] == 'E':
            self.X += int(d[1:])
        elif d[0] == 'W':
            self.X -= int(d[1:])
        elif d[0] == 'R':
            self.angle -= int(d[1:])
            self.angle %= 360
        elif d[0] == 'L':
            self.angle += int(d[1:])
            self.angle %= 360
        elif d[0] == 'F':
            if self.angle == 0:
                self.X += int(d[1:])
            elif self.angle == 90:
                self.Y += int(d[1:])
            elif self.angle == 180:
                self.X -= int(d[1:])
            elif self.angle == 270:
                self.Y -= int(d[1:])

    def getDist(self):
        return sum([abs(self.X), abs(self.Y)])


def partOne(f: TextIOWrapper):
    directions = f.read().strip().split('\n')

    ship = Ship1()
    for d in directions:
        ship.readInput(d)
    return ship.getDist()


def partTwo(f: TextIOWrapper):
    pass


if __name__ == '__main__':
    with open('12.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
