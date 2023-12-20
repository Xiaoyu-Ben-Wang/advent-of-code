from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    card_values = {"T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}

    def getHandScore(hand: str):
        if len(set(hand)) == 1:
            return 7
        if len(set(hand)) == 2:
            first = set(hand).pop()
            second = set(hand).pop()
            first_count = hand.count(first)
            second_count = hand.count(second)
            if first_count == 4 or first_count == 1:
                return 6
            else:
                return 5

        for card in hand:
            if hand.count(card) == 3:
                return 4
        if len(set(hand)) == 3:
            return 3
        for card in hand:
            if hand.count(card) == 2:
                return 2
        return 1

    def getCardValueScore(hand: str):
        total_val = 0
        for i, letter in enumerate(hand[::-1]):
            if letter.isdigit():
                total_val += (int(letter) - 1) * 14**i
            else:
                total_val += card_values[letter] * 14**i
        return total_val

    all_hands = []
    for line in f.readlines():
        hand, value = line.strip().split()
        all_hands.append((getHandScore(hand), getCardValueScore(hand), hand, value))
    score = 0

    for i, data in enumerate(sorted(all_hands)):
        score += (i + 1) * int(data[-1])

    return score


def partTwo(f: TextIOWrapper):
    card_values = {"J": 1, "T": 9, "Q": 10, "K": 11, "A": 12}

    def getCardValueScore(hand: str):
        total_val = 0
        for i, letter in enumerate(hand[::-1]):
            if letter.isdigit():
                total_val += (int(letter)) * 13**i
            else:
                total_val += card_values[letter] * 13**i
        return total_val

    def getHandScore(hand: str):
        if len(set(hand)) == 1:
            return 7
        if len(set(hand)) == 2:
            first = set(hand).pop()
            first_count = hand.count(first)
            if first_count == 4 or first_count == 1:
                return 6
            else:
                return 5

        for card in hand:
            if hand.count(card) == 3:
                return 4
        if len(set(hand)) == 3:
            return 3
        for card in hand:
            if hand.count(card) == 2:
                return 2
        return 1

    all_hands = []
    for line in f.readlines():
        hand, value = line.strip().split()
        all_hands.append((getHandScore(hand), getCardValueScore(hand), hand, value))
    score = 0

    for i, data in enumerate(sorted(all_hands)):
        score += (i + 1) * int(data[-1])

    return score


if __name__ == "__main__":
    with open("2023_7.txt") as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 [{timedelta(seconds=end-start)}]: {ans}")

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 2 [{timedelta(seconds=end-start)}]: {ans}")
