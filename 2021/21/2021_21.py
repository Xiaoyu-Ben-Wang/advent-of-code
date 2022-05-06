from timeit import default_timer as timer
from datetime import date, timedelta

class DDice:
    def __init__(self) -> None:
        self.val = 1
        self.rollCount = 0

    def roll3(self):
        vals = []
        for _ in range(3):
            vals.append(self.val)
            self.val = self.val % 100 + 1
            self.rollCount += 1
        return vals

def partOne(f):
    data = [int(line.split(' ')[-1]) for line in f.read().splitlines()]

    dice = DDice()

    pos1 = data[0]
    pos2 = data[1]
    score1 = 0
    score2 = 0
    turn = 0


    while score1 < 1000 and score2 < 1000:
        # p1 roll
        change = dice.roll3()
        if turn == 0:
            for _ in range(sum(change)):
                pos1 = (pos1) % 10 + 1
            score1 += pos1
        else:
            for _ in range(sum(change)):
                pos2 = (pos2) % 10 + 1
            score2 += pos2

        turn = (turn+1)%2

    print(dice.rollCount)
    return min(score1, score2) * dice.rollCount



def partTwo(f):
    positions = [int(line.split(' ')[-1]) for line in f.read().splitlines()]
    pos1 = positions[0]
    pos2 = positions[1]
    # post to possible scores
    WIN_SCORE = 21
    possible_scores = dict()
    for i in range(1,11):
        v1 = i % 10 + 1
        v2 = v1 % 10 + 1
        v3 = v2 % 10 + 1
        possible_scores[i] = (v1, v2, v3)

    hashmap = dict()

    def findWins(pos1, pos2, score1= 0, score2 = 0):
        count1 = 0
        count2 = 0



    return count1, count2



if __name__ == '__main__':
    with open('21.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')