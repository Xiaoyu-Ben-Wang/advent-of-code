from timeit import default_timer as timer
from datetime import timedelta

class Board:
    def __init__(self, data) -> None:
        self.size = 0
        self.board = []
        self.marked = []
        for line in data.split('\n'):
            self.board.append([int(n) for n in line.split()])
            self.marked.append([0 for n in line.split()])
        self.size = len(self.board)

    def markNum(self, num):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == num:
                    self.marked[i][j] = 1

    def checkWin(self) -> bool:
        for i in range(self.size):
            if sum(self.marked[i]) == self.size:
                return True
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                count += self.marked[j][i]
            if count == self.size:
                return True
        return False


    def getScore(self, lastInput) -> int:
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.marked[i][j] == 0:
                    count += self.board[i][j]
        return count*lastInput

def partOne(f):
    text = f.read().split('\n\n')
    nums, boards_list = [int(n) for n in text[0].split(',')], text[1:]
    boards_list = [Board(b) for b in boards_list]
    for n in nums:
        for board in boards_list:
            board.markNum(n)
            if board.checkWin():
                return board.getScore(n)

def partTwo(f):
    text = f.read().split('\n\n')
    nums, boards_list = [int(n) for n in text[0].split(',')], text[1:]
    boards_list = [Board(b) for b in boards_list]
    for n in nums:
        won = set()
        for board in boards_list:
            board.markNum(n)
            if board.checkWin():
                won.add(board)
        if len(boards_list)==1:
            if boards_list[0].checkWin():
                return boards_list[0].getScore(n)
        else:
            for b in won:
                boards_list.remove(b)


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
