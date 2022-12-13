import re
from datetime import timedelta
from io import TextIOWrapper
from timeit import default_timer as timer


def partOne(f: TextIOWrapper):
    inp = f.read()
    boxes, instructions = inp.split('\n\n')
    boxes = boxes.split('\n')
    columns = [list() for _ in re.findall(r'\d', boxes[-1])]
    for line in boxes[:-1]:
        for i in range(len(columns)):
            box = re.search(r'\[(.)\]', line[i*4:i*4+4])
            if box is not None:
                columns[i].insert(0, box.group(1))

    for ins in instructions.split('\n'):

        vals = re.search(r'move (\d+) from (\d+) to (\d+)', ins)
        if vals is not None:
            vals = vals.groups()
            for _ in range(int(vals[0])):
                if len(columns[int(vals[1])-1]) > 0:
                    temp = columns[int(vals[1])-1].pop()
                    columns[int(vals[2])-1].append(temp)

    return ''.join(c[-1] if len(c) > 0 else '' for c in columns)


def partTwo(f: TextIOWrapper):
    inp = f.read()
    boxes, instructions = inp.split('\n\n')
    boxes = boxes.split('\n')
    columns = [list() for _ in re.findall(r'\d', boxes[-1])]
    for line in boxes[:-1]:
        for i in range(len(columns)):
            box = re.search(r'\[(.)\]', line[i*4:i*4+4])
            if box is not None:
                columns[i].insert(0, box.group(1))

    for ins in instructions.split('\n'):

        vals = re.search(r'move (\d+) from (\d+) to (\d+)', ins)
        if vals is not None:
            vals = vals.groups()
            temp = columns[int(vals[1])-1][-int(vals[0]):]
            columns[int(vals[1])-1] = columns[int(vals[1])-1][:-int(vals[0])]
            columns[int(vals[2])-1].extend(temp)

    return ''.join(c[-1] if len(c) > 0 else '' for c in columns)


if __name__ == '__main__':
    with open('2022_5.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
