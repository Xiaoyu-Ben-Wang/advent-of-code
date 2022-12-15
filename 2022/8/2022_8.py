from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    trees = [[int(n) for n in row.strip()] for row in f.readlines()]
    visible = [[0 for _ in row] for row in trees]
    # rows
    for row in range(len(trees)):
        lowest = -1
        for col in range(len(trees[row])):
            if trees[row][col] > lowest:
                lowest = trees[row][col]
                visible[row][col] = 1

        lowest = -1
        for col in reversed(range(len(trees[row]))):
            if trees[row][col] > lowest:
                lowest = trees[row][col]
                visible[row][col] = 1
    # columns
    for col in range(len(trees[0])):
        lowest = -1
        for row in range(len(trees)):
            if trees[row][col] > lowest:
                lowest = trees[row][col]
                visible[row][col] = 1
        lowest = -1
        for row in reversed(range(len(trees))):
            if trees[row][col] > lowest:
                lowest = trees[row][col]
                visible[row][col] = 1
    return sum(sum(row) for row in visible)


def partTwo(f: TextIOWrapper):
    trees = [[int(n) for n in row.strip()] for row in f.readlines()]
    location_scores = [[0 for _ in row] for row in trees]

    for row in range(len(trees)):
        for col in range(len(trees[row])):
            height = trees[row][col]
            scores = [0, 0, 0, 0]
            for i in range(row+1, len(trees)):
                if trees[i][col] < height:
                    scores[0] += 1
                elif trees[i][col] >= height:
                    scores[0] += 1
                    break
            for i in range(row-1, -1, -1):
                if trees[i][col] < height:
                    scores[1] += 1
                elif trees[i][col] >= height:
                    scores[1] += 1
                    break
            for i in range(col+1, len(trees[row])):
                if trees[row][i] < height:
                    scores[2] += 1
                elif trees[row][i] >= height:
                    scores[2] += 1
                    break
            for i in range(col-1, -1, -1):
                if trees[row][i] < height:
                    scores[3] += 1
                elif trees[row][i] >= height:
                    scores[3] += 1
                    break
            location_scores[row][col] = scores[0]*scores[1]*scores[2]*scores[3]
    return max(max(row) for row in location_scores)


if __name__ == '__main__':
    with open('2022_8.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
