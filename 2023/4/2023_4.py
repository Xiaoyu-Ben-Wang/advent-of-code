from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
import re


def partOne(f: TextIOWrapper):
    score = 0
    for line in f.readlines():
        win_str, num_str = re.findall(r'((?:\d+\s+){2,})', line)
        winning = set(int(n) for n in win_str.split())
        numbers = list(int(n) for n in num_str.split())
        points = 0
        for n in numbers:
            if n in winning:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        score += points

    return score


def partTwo(f: TextIOWrapper):
    # card_points = {}
    lines = f.readlines()
    card_counts = [1 for _ in range(len(lines))]

    for line in lines:
        game_num, win_str, num_str = re.findall(r'((?:\d+\s*)+)', line)
        winning = set(int(n) for n in win_str.split())
        numbers = list(int(n) for n in num_str.split())
        points = 0
        for n in numbers:
            if n in winning:
                points += 1
        # card_points[int(game_num)] = points
        game_num = int(game_num)
        for i in range(game_num, game_num+points):
            card_counts[i] += card_counts[game_num-1]

    return sum(card_counts)


if __name__ == '__main__':
    with open('2023_4.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
