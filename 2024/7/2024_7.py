from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import re


def partOne(f: TextIOWrapper):
    count = 0

    def canSolve(goal, curr, remaining_nums):
        if len(remaining_nums) == 0:
            if goal == curr:
                return True
            return False
        new_remaining = remaining_nums.copy()
        new_val = new_remaining.pop(0)
        return canSolve(goal, curr + new_val, new_remaining[:]) or canSolve(goal, curr * new_val, new_remaining[:])
    for line in f.read().splitlines():
        match = re.findall(r'(\d+): ((?:\d+ ?)+)', line)[0]

        goal = int(match[0])
        nums = [int(n) for n in match[1].split()]

        if canSolve(goal, nums[0], nums[1:]):
            count += goal
    return count


def partTwo(f: TextIOWrapper):
    count = 0

    def canSolve(goal, curr, remaining_nums):
        if len(remaining_nums) == 0:
            if goal == curr:
                return True
            return False
        new_remaining = remaining_nums.copy()
        new_val = new_remaining.pop(0)
        return canSolve(goal, curr + new_val, new_remaining[:]) or canSolve(goal, curr * new_val, new_remaining[:]) or canSolve(goal, int(str(curr)+str(new_val)), new_remaining[:])
    for line in f.read().splitlines():
        match = re.findall(r'(\d+): ((?:\d+ ?)+)', line)[0]

        goal = int(match[0])
        nums = [int(n) for n in match[1].split()]

        if canSolve(goal, nums[0], nums[1:]):
            count += goal
    return count


if __name__ == '__main__':
    with open('2024_7.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
