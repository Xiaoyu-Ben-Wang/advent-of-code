from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def isValid1(num):
    string = str(num)
    double_found = False
    for index in range(len(string)-1):
            if int(string[index]) > int(string[index+1]):
                return False
            if string[index] == string[index+1]:
                double_found = True

    return double_found

def isValid2(num):
    string = str(num)
    double_found = False
    for index in range(len(string)-1):
            if int(string[index]) > int(string[index+1]):
                return False
            if string[index] == string[index+1]:
                if index > 0 and string[index-1] == string[index]:
                    continue
                if index+2 < len(string) and string[index] == string[index+2]:
                    continue
                double_found = True
    return double_found


def partOne(f: TextIOWrapper):
    start, end = [int(n) for n in f.read().strip().split('-')]
    total = 0
    for n in range(start, end+1):
        if isValid1(n):
            total += 1
    return total
        



def partTwo(f: TextIOWrapper):
    start, end = [int(n) for n in f.read().strip().split('-')]
    total = 0
    for n in range(start, end+1):
        if isValid2(n):
            total += 1
    return total


if __name__ == '__main__':
    with open('2019_4.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')