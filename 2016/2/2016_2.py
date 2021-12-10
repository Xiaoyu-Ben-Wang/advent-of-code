from timeit import default_timer as timer


def partOne(f):
    keyPad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    ans = ''
    code = f.read().strip().split('\n')
    for line in code:
        pos = [1, 1]
        for c in line:
            if c == 'U':
                if pos[0] != 0:
                    pos[0] -= 1
            elif c == 'D':
                if pos[0] != 2:
                    pos[0] += 1
            elif c == 'L':
                if pos[1] != 0:
                    pos[1] -= 1
            elif c == 'R':
                if pos[1] != 2:
                    pos[1] += 1
        ans += str(keyPad[pos[0]][pos[1]])
    return ans


def partTwo(f):
    keyPad = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, 'A', 'B', 'C', 0],
        [0, 0, 'D', 0, 0]
    ]

    ans = ''
    code = f.read().strip().split('\n')
    for line in code:
        pos = [2, 0]
        for c in line:
            if c == 'U':
                if pos[0] != 0 and keyPad[pos[0]-1][pos[1]] != 0:
                    pos[0] -= 1
            elif c == 'D':
                if pos[0] != 4 and keyPad[pos[0]+1][pos[1]] != 0:
                    pos[0] += 1
            elif c == 'L':
                if pos[1] != 0 and keyPad[pos[0]][pos[1]-1] != 0:
                    pos[1] -= 1
            elif c == 'R':
                if pos[1] != 4 and keyPad[pos[0]][pos[1]+1] != 0:
                    pos[1] += 1
        ans += str(keyPad[pos[0]][pos[1]])
    return ans


if __name__ == '__main__':
    with open('2.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f"Part 1 Answer: {ans} ({(end-start)*1000:.5f} ms)")
        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f"Part 1 Answer: {ans} ({(end-start)*1000:.5f} ms)")
