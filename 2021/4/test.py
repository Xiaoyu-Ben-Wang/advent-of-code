with open("4.txt", "r") as f:
    lines = f.readlines()


bingo_numbers = [int(num) for num in lines.pop(0).split(",")]
assert len(lines) % 6 == 0
n_boards = len(lines) // 6
bingo_boards = [
    [[int(num) for num in line.split()] for line in lines[6 * i + 1: 6 * (i + 1)]]
    for i in range(n_boards)
]


def has_won(board, called_numbers):
    return any(all(num in called_numbers for num in line) for line in [*board, *zip(*board)])


def score(board, called_numbers, last_number):
    return last_number * sum(num for line in board for num in line if num not in called_numbers)


# Part 1
def find_score_of_first_bingo_winner(numbers, boards):
    called_numbers = set()
    for num in numbers:
        called_numbers.add(num)
        for board in boards:
            if has_won(board, called_numbers):
                return score(board, called_numbers, num)
    return -1


print(find_score_of_first_bingo_winner(bingo_numbers, bingo_boards))


# Part 2
def find_score_of_last_bingo_winner(numbers, boards):
    called_numbers = set()
    for num in numbers:
        called_numbers.add(num)
        if len(boards) == 1 and has_won(boards[0], called_numbers):
            return score(boards[0], called_numbers, num)
        boards = [board for board in boards if not has_won(board, called_numbers)]
    return -1


print("Part 1", find_score_of_first_bingo_winner(bingo_numbers, bingo_boards))
print("Part 2", find_score_of_last_bingo_winner(bingo_numbers, bingo_boards))
