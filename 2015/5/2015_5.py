from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    strings = f.read().split()

    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_strings = 0
    for string in strings:
        # vowels part
        cond1 = False
        v_count = 0
        for v in vowels:
            v_count += string.count(v)
            if v_count >= 3:
                cond1 = True
                break

        # twice in a row
        cond2 = False
        for i in range(1, len(string)):
            if string[i] == string[i-1]:
                cond2 = True
                break

        # nonvalid strings
        cond3 = True
        nonvalid = ['ab', 'cd', 'pq', 'xy']
        for n in nonvalid:
            if n in string:
                cond3 = False
                break
        if cond1 and cond2 and cond3:
            valid_strings += 1

    return valid_strings


def partTwo(f):
    strings = f.read().split()
    valid_strings = 0
    for string in strings:
        cond1 = False
        for i in range(len(string)-1):
            if string.count(string[i:i+2]) >= 2:
                cond1 = True
                break
        cond2 = False
        for i in range(len(string)-2):
            if string[i] == string[i+2]:
                cond2 = True
                break
        if cond1 and cond2:
            valid_strings += 1
    return valid_strings


if __name__ == '__main__':
    with open("5.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
