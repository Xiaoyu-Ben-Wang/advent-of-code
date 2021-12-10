from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    phrases = f.read().strip().split('\n')
    valid = 0
    for phrase in phrases:
        words = phrase.split()
        duplicate = False
        for w in words:
            if words.count(w)>1:
                duplicate = True
        if not duplicate:
            valid += 1
    return valid



def partTwo(f):
    phrases = f.read().strip().split('\n')
    valid = 0
    for phrase in phrases:
        words = [''.join(sorted(w)) for w in phrase.split()]
        duplicate = False
        for w in words:
            if words.count(w)>1:
                duplicate = True
        if not duplicate:
            valid += 1
    return valid


if __name__ == '__main__':
    with open("4.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")