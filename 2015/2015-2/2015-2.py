
def main():
    print('=== 2015 Day 2 ===')
    print("Part 1:", part1())
    print("Part 2:", part2())


def part1():
    with open("2015-2.txt") as file:
        lines = file.readlines()
        total =0
        for line in lines:
            dim = line.strip().split('x')
            areas = [2*int(dim[0])*int(dim[1]), 2*int(dim[1])*int(dim[2]), 2*int(dim[0])*int(dim[2])]
            total += sum(areas) + min(areas)//2
        return total


def part2():
    with open("2015-2.txt") as file:
        lines = file.readlines()
        total =0
        for line in lines:
            dim = line.strip().split('x')
            permts = [2*int(dim[0])+2*int(dim[1]), 2*int(dim[1])+2*int(dim[2]), 2*int(dim[0])+2*int(dim[2])]
            total += min(permts) + int(dim[0])*int(dim[1])*int(dim[2])
        return total



if __name__=='__main__':
    main()