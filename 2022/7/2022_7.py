from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    commands = [line.strip() for line in f.readlines()]
    position = []
    directories = dict()

    while len(commands) > 0:
        command = commands.pop(0)
        if command[:5] == '$ cd ':
            new_dir = command[5:]
            if new_dir == '..':
                position.pop()
            else:
                position.append(new_dir)
                pos_string = '/'.join(position)
                if new_dir not in directories:
                    directories[pos_string] = []
        if command[:5] == '$ ls':
            pos_string = '/'.join(position)
            while len(commands) > 0 and commands[0][0] != '$':
                left, right = commands.pop(0).split()
                if left == 'dir':
                    directories[pos_string].append(pos_string+'/'+right)
                else:
                    directories[pos_string].append(int(left))

    directory_sizes = dict()
    find_pos = ['/']

    def findDirectorySums():
        while find_pos:
            pos = find_pos[-1]
            while directories[pos]:
                item = directories[pos].pop()

                if isinstance(item, int):
                    directory_sizes[pos] = directory_sizes.get(pos, 0)+item
                else:
                    if item in directory_sizes:
                        directory_sizes[pos] = directory_sizes.get(pos, 0)+directory_sizes[item]
                    else:
                        directories[pos].append(item)
                        find_pos.append(item)
                        break
            if len(directories[pos]) == 0:
                find_pos.pop()

    findDirectorySums()
    total = 0

    for size in directory_sizes.values():
        if size <= 100000:
            total += size
    return total


def partTwo(f: TextIOWrapper):
    DISK_SPACE = 70000000
    REQUIRED_SPACE = 30000000

    commands = [line.strip() for line in f.readlines()]
    position = []
    directories = dict()

    while len(commands) > 0:
        command = commands.pop(0)
        if command[:5] == '$ cd ':
            new_dir = command[5:]
            if new_dir == '..':
                position.pop()
            else:
                position.append(new_dir)
                pos_string = '/'.join(position)
                if new_dir not in directories:
                    directories[pos_string] = []
        if command[:5] == '$ ls':
            pos_string = '/'.join(position)
            while len(commands) > 0 and commands[0][0] != '$':
                left, right = commands.pop(0).split()
                if left == 'dir':
                    directories[pos_string].append(pos_string+'/'+right)
                else:
                    directories[pos_string].append(int(left))

    directory_sizes = dict()
    find_pos = ['/']

    def findDirectorySums():
        while find_pos:
            pos = find_pos[-1]
            while directories[pos]:
                item = directories[pos].pop()

                if isinstance(item, int):
                    directory_sizes[pos] = directory_sizes.get(pos, 0)+item
                else:
                    if item in directory_sizes:
                        directory_sizes[pos] = directory_sizes.get(pos, 0)+directory_sizes[item]
                    else:
                        directories[pos].append(item)
                        find_pos.append(item)
                        break
            if len(directories[pos]) == 0:
                find_pos.pop()

    findDirectorySums()
    total = 0

    delete_space = REQUIRED_SPACE - (DISK_SPACE-directory_sizes['/'])
    min_ans = float('inf')
    for size in directory_sizes.values():
        if size >= delete_space and size < min_ans:
            min_ans = size
    return min_ans


if __name__ == '__main__':
    with open('2022_7.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
