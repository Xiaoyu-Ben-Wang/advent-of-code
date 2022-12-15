from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    regx = 1
    cycle = 1
    waiting = False
    strengths = []

    commands = [line.strip() for line in f.readlines()]
    while len(commands) > 0:
        if 'noop' in commands[0]:
            commands.pop(0)
        elif 'addx' in commands[0]:
            if waiting:
                regx += int(commands[0].split()[1])
                waiting = False
                commands.pop(0)
            else:
                waiting = True


        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            strengths.append(cycle*regx)

    return sum(strengths)


def partTwo(f: TextIOWrapper):
    regx = 1
    cycle = 1
    waiting = False
    strengths = []

    commands = [line.strip() for line in f.readlines()]

    output = ['#']
    while len(commands) > 0:
        if 'noop' in commands[0]:
            commands.pop(0)
        elif 'addx' in commands[0]:
            if waiting:
                regx += int(commands[0].split()[1])
                waiting = False
                commands.pop(0)
            else:
                waiting = True


        cycle += 1


        if (cycle-1) % 40 >= regx -1 and (cycle-1) % 40 <= regx + 1:
            output.append('#')
        else:
            output.append('.')
        if (cycle) % 40 == 0:
            output.append('\n')

    print(''.join(output))


if __name__ == '__main__':
    with open('2022_10.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')