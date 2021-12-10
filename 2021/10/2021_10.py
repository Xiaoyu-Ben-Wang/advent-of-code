from timeit import default_timer as timer
from datetime import timedelta


def partOne(f):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    match = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>',
    }

    data = [line.strip() for line in f.read().split()]
    score = 0

    for line in data:
        stack = []
        for c in line:
            if c in match:
                stack.append(match[c])
            else:
                endchar = stack.pop()
                if endchar != c:
                    score += points[c]
                    break
    return score


def partTwo(f):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    match = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>',
    }

    data = [line.strip() for line in f.read().split()]
    scoreList = []

    for line in data:
        stack = []
        corrupted= False
        line_score = 0
        for c in line:
            if c in match:
                stack.append(match[c])
            else:
                endchar = stack.pop()
                if endchar != c:
                    corrupted = True
                    break
        if not corrupted and len(stack)!=0:
            while len(stack) != 0:
                line_score *= 5
                line_score += points[stack.pop()]
            scoreList.append(line_score)
    scoreList.sort()
    return scoreList[len(scoreList)//2]

if __name__ == '__main__':
    with open('10.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
