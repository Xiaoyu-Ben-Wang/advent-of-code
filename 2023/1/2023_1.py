from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    def firstDigit(string):
        for s in string:
            if s.isdigit():
                return int(s)

    def lastDigit(string):
        for s in reversed(string):
            if s.isdigit():
                return int(s)

    return sum(10*firstDigit(n)+lastDigit(n) for n in f.readlines())


def partTwo(f: TextIOWrapper):

    numbers = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'zero': 0,
    }

    def firstDigit(string):
        l = 1
        start = 0
        while True:
            while l < len(string) - 1:
                if string[start:start+l].isdigit():
                    return int(string[start:start+l])
                if string[start:start+l] in numbers:
                    return numbers[string[start:start+l]]
                l += 1
            start += 1
            l = 1

    def lastDigit(string):
        l = 1
        start = len(string)
        while True:
            while l < len(string) - 1:
                if string[start-l:start].isdigit():
                    return int(string[start-l:start])
                if string[start-l:start] in numbers:
                    return numbers[string[start-l:start]]
                l += 1
            start -= 1
            l = 1
    return sum(10*firstDigit(n)+lastDigit(n) for n in f.readlines())


if __name__ == '__main__':
    with open('2023_1.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
