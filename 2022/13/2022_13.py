from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
from ast import literal_eval


def evaluate(left, right):
    if type(left) is int and type(right) is int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    elif type(left) is list and type(right) is int:
        return evaluate(left, [right])
    elif type(left) is int and type(right) is list:
        return evaluate([left], right)
    elif type(left) is list and type(right) is list:
        index = -1
        while index < max(len(left), len(right)):
            index += 1
            if index >= len(left) and index >= len(right):
                return None
            elif index >= len(left):
                return True
            elif index >= len(right):
                return False
            else:
                result = evaluate(left[index], right[index])
                if result != None:
                    return result

    raise Exception(f"Unexpected value: {left}, {right}")


def partOne(f: TextIOWrapper):
    pairs = [(literal_eval(left), literal_eval(right)) for left, right in [group.split('\n') for group in f.read().split('\n\n')]]

    total = 0
    for i, (left, right) in enumerate(pairs):
        if evaluate(left, right):
            total += i+1
    return total


def partTwo(f: TextIOWrapper):
    pairs = [(literal_eval(left), literal_eval(right)) for left, right in [group.split('\n') for group in f.read().split('\n\n')]]

    all_pairs = []

    for pair in pairs:
        all_pairs.extend(pair)

    all_pairs.append([[2]])
    all_pairs.append([[6]])

    # sort
    while True:
        swapped = False
        for i in range(len(all_pairs)-1):
            if not evaluate(all_pairs[i], all_pairs[i+1]):
                swapped = True
                temp = all_pairs[i]
                all_pairs[i] = all_pairs[i+1]
                all_pairs[i+1] = temp
        if swapped is False:
            break

    div1 = None
    div2 = None

    for i, pair in enumerate(all_pairs):
        if str(pair) == str([[2]]):
            div1 = i+1
        if str(pair) == str([[6]]):
            div2 = i+1

    return div1*div2


if __name__ == '__main__':
    with open('2022_13.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
