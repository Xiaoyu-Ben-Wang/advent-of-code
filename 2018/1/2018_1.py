from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    freq = 0
    for l in f.read().split('\n'):
        freq += int(l)
    return freq


def partTwo(f):
    freq = 0
    freq_list = {0}
    instructions = f.read().split('\n')
    length = len(instructions)
    i = 0
    while True:
        freq += int(instructions[i])
        i = (i+1) % length
        if freq in freq_list:
            return freq
        else:
            freq_list.add(freq)


if __name__ == '__main__':
    with open("1.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
