from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    bits = f.read().splitlines()
    gamma = [0 for _ in bits[0]]
    for bit in bits:
        for i in range(len(bit)):
            if bit[i] == '1':
                gamma[i] += 1
            elif bit[i] == '0':
                gamma[i] -= 1
    for i in range(len(gamma)):
        if gamma[i] > 0:
            gamma[i] = 1
        elif gamma[i] < 0:
            gamma[i] = 0
    epsilon = [(n+1) % 2 for n in gamma]
    return int(''.join([str(n) for n in epsilon]), 2)*int(''.join([str(n) for n in gamma]), 2)


def partTwo(f):

    oxy = f.read().splitlines()
    co2 = oxy[:]
    for i in range(len(oxy[0])):
        if len(oxy) != 1:
            common = mostCommonBit(oxy, i)
            oxy = list(filter(lambda x: int(x[i]) == common, oxy))

        if len(co2) != 1:
            least = leastCommonBit(co2, i)
            co2 = list(filter(lambda x: int(x[i]) == least, co2))

    return int(oxy[0], 2)*int(co2[0], 2)


def mostCommonBit(arr, bit):
    count = 0
    for line in arr:
        if line[bit] == '1':
            count += 1
        else:
            count -= 1
    return 1 if (count >= 0) else 0


def leastCommonBit(arr, bit):
    count = 0
    for line in arr:
        if line[bit] == '1':
            count += 1
        else:
            count -= 1
    return 0 if (count >= 0) else 1


if __name__ == '__main__':
    with open("3.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
