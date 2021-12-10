
def main():
    print('=== 2015 Day 3 ===')
    print("Part 1:", part1())
    print("Part 2:", part2())


def part1():
    houses = set()
    with open("2015-3.txt") as file:
        pos = (0,0)
        houses.add(pos)
        text = file.read().replace('\n','')
        for l in text:
            if l == '^':
                pos = (pos[0],pos[1]+1)
            elif l =='v':
                pos = (pos[0],pos[1]-1)
            elif l =='<':
                pos = (pos[0]-1,pos[1])
            elif l =='>':
                pos = (pos[0]+1,pos[1])
            houses.add(pos)
        return len(houses)


def part2():
    houses = set()
    with open("3.txt") as file:
        santa = (0,0)
        robo = (0,0)
        houses.add(santa)
        text = file.read().replace('\n','')
        for i in range(len(text)):
            l = text[i]
            if i%2:
                if l == '^':
                    robo = (robo[0],robo[1]+1)
                elif l =='v':
                    robo = (robo[0],robo[1]-1)
                elif l =='<':
                    robo = (robo[0]-1,robo[1])
                elif l =='>':
                    robo = (robo[0]+1,robo[1])
                houses.add(robo)
            else:
                if l == '^':
                    santa = (santa[0],santa[1]+1)
                elif l =='v':
                    santa = (santa[0],santa[1]-1)
                elif l =='<':
                    santa = (santa[0]-1,santa[1])
                elif l =='>':
                    santa = (santa[0]+1,santa[1])
                houses.add(santa)
        return len(houses)



if __name__=='__main__':
    main()