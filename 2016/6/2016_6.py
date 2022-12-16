from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    lines = [line.strip() for line in f.readlines()]
    columns = [[line[i] for line in lines] for i in range(len(lines[0]))]
    msg = []
    for col in columns:
        counter = dict()
        for c in col:
            counter[c] = counter.get(c, 0)+ 1
        msg.append(sorted(counter.items(), key=lambda item: item[1])[-1][0])
    return ''.join(msg)



def partTwo(f: TextIOWrapper):
    lines = [line.strip() for line in f.readlines()]
    columns = [[line[i] for line in lines] for i in range(len(lines[0]))]
    msg = []
    for col in columns:
        counter = dict()
        for c in col:
            counter[c] = counter.get(c, 0)+ 1
        msg.append(sorted(counter.items(), key=lambda item: item[1])[0][0])
    return ''.join(msg)


if __name__ == '__main__':
    with open('2016_6.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')