from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta

'''
ABC = RPS
XYZ = RPS
'''

win_points = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

choice_points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

win_choice = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

draw_choice = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

lose_choice = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}


def partOne(f: TextIOWrapper):
    moves = [(m.split()[0], m.split()[1]) for m in f.readlines()]
    score = 0
    for m in moves:
        score += win_points[m] + choice_points[m[1]]
    return score


def partTwo(f: TextIOWrapper):
    moves = [(m.split()[0], m.split()[1]) for m in f.readlines()]
    score = 0
    for m in moves:
        if m[1] == 'X':
            # lose
            score += choice_points[lose_choice[m[0]]] + 0
        elif m[1] == 'Y':
            # draw
            score += choice_points[draw_choice[m[0]]] + 3
        elif m[1] == 'Z':
            # win
            score += choice_points[win_choice[m[0]]] + 6
    return score


if __name__ == '__main__':
    with open('2022_2.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
