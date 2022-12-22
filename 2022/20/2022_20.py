from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta
from tqdm import tqdm


class Node:
    def __init__(self, val, prev=None, nextt=None) -> None:
        self.val = val
        self.next = nextt
        self.prev = prev


class Num:
    def __init__(self, index, value) -> None:
        self.index = index
        self.value = value

    def __repr__(self) -> str:
        return f'[index: {self.index}, value: {self.value}]'


def printInOrder(arr: list):
    out = [None for _ in range(len(arr))]
    for n in arr:
        out[n.index] = n.value
    print(out)


def getEnd(start: int, diff: int, length: int):
    return (start+diff) % (length - 1)
    # actual_diff = diff % (length-1)

    # if actual_diff > 0:
    #     for _ in range(actual_diff):
    #         start = (start+1) % length
    #         if start == 0:
    #             start += 1
    # elif actual_diff < 0:
    #     # return ((start+diff) % length - (-diff-start)//length) % length
    #     for _ in range(-actual_diff):
    #         start = (start-1) % length
    #         if start == length-1:
    #             start -= 1
    return start


def partOne(f: TextIOWrapper):

    numbers = [int(n) for n in f.read().splitlines()]

    order = []
    num_index_to_order_location = dict()

    for i, val in enumerate(numbers):
        num = Num(i, val)
        order.append(num)
        num_index_to_order_location[i] = i

    for i in tqdm(range(len(order))):
        new_order = [Num(n.index, n.value) for n in order]
        num = order[i]
        start = num.index
        diff = num.value
        end_goal = getEnd(start, diff, len(order))

        if diff == 0:
            continue

        if end_goal > start:
            while start != end_goal:
                start = (start+1)
                # find start
                location_in_order = num_index_to_order_location[start]

                new_order[location_in_order].index -= 1
            new_order[i].index = end_goal

        elif end_goal < start:
            while start != end_goal:
                start = (start - 1)
                location_in_order = num_index_to_order_location[start]

                new_order[location_in_order].index += 1
            new_order[i].index = end_goal

        order = new_order
        for index, num in enumerate(order):
            num_index_to_order_location[num.index] = index

    ans = [None for _ in range(len(order))]
    for n in order:
        ans[n.index] = n.value

    return ans[(ans.index(0)+1000) % len(ans)]+ans[(ans.index(0)+2000) % len(ans)]+ans[(ans.index(0)+3000) % len(ans)]


def mix(numbers):

    order = []
    num_index_to_order_location = dict()

    for i, val in enumerate(numbers):
        num = Num(i, val)
        order.append(num)
        num_index_to_order_location[i] = i

    for i in (range(len(order))):
        new_order = [Num(n.index, n.value) for n in order]
        num = order[i]
        start = num.index
        diff = num.value
        end_goal = getEnd(start, diff, len(order))

        if diff % (len(order)-1) == 0:
            continue

        if end_goal > start:
            while start != end_goal:
                start = (start+1)
                # find start
                location_in_order = num_index_to_order_location[start]

                new_order[location_in_order].index -= 1
            new_order[i].index = end_goal

        elif end_goal < start:
            while start != end_goal:
                start = (start - 1)
                location_in_order = num_index_to_order_location[start]

                new_order[location_in_order].index += 1
            new_order[i].index = end_goal

        order = new_order
        for index, num in enumerate(order):
            num_index_to_order_location[num.index] = index

    ans = [None for _ in range(len(order))]
    for n in order:
        ans[n.index] = n.value

    return ans


def partTwo(f: TextIOWrapper):
    KEY = 811589153
    numbers = [int(n)*KEY for n in f.read().splitlines()]
    print(numbers)
    for _ in range(10):

        numbers = mix(numbers)
        print(numbers)
    return numbers[(numbers.index(0)+1000) % (len(numbers))]+numbers[(numbers.index(0)+2000) % len(numbers)]+numbers[(numbers.index(0)+3000) % len(numbers)]


if __name__ == '__main__':
    with open('2022_20.txt') as f:
        start = timer()
        numbers = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {numbers}')

        f.seek(0)
        start = timer()
        numbers = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {numbers}')
