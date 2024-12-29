from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    data = '2333133121414131402'
    formatted = []
    left = 0
    right = len(data) - 1
    right_leftover = []
    if right % 2 != 0:
        right -= 1
    # right is on data for sure
    while left < right:
        # insert data on the left
        left_n = int(data[left])
        left_value = left//2
        formatted.extend([left_value]*left_n)

        left += 1
        free_spaces = int(data[left])
        while free_spaces > 0:
            print(formatted)
            if len(right_leftover) >= free_spaces:
                formatted.extend(right_leftover[:free_spaces])
                right_leftover = right_leftover[:len(right_leftover)-free_spaces]
                free_spaces = 0
                continue
            elif len(right_leftover) > 0:
                free_spaces -= len(right_leftover)
                formatted.extend(right_leftover)
                right_leftover = []
                continue

            right_n = int(data[right])
            right_value = right // 2
            if right_n > free_spaces:
                formatted.extend([right_value]*free_spaces)
                right_leftover = [right_value]*(right_n-free_spaces)
                free_spaces = 0
            else:
                free_spaces -= right_n
                formatted.extend([right_value]*right_n)
                right -= 2
        left += 1
    checksum = 0
    for i, val in enumerate(formatted):
        checksum += i*val
    return checksum


def partTwo(f: TextIOWrapper):
    pass


if __name__ == '__main__':
    with open('2024_9.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
