from timeit import default_timer as timer

# Part 1


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


def partOne(f):
    directions = f.read().strip().split('\n')

    ship = Ship1()
    for d in directions:
        ship.readInput(d)
    return ship.getDist()


if __name__ == '__main__':
    with open('12.txt') as f:
        start1 = timer()
        ans = partOne(f)
        end1 = timer()
        print(f"Part 1 Answer: {ans} ({(end1-start1)*1000:.5f} ms)")
