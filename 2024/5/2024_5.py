from io import TextIOWrapper
from timeit import default_timer as timer
from datetime import timedelta


def partOne(f: TextIOWrapper):
    rules, pages = f.read().split('\n\n')
    result = 0
    befores = dict()
    for rule in rules.split():
        prev, after = rule.split('|')
        prev, after = int(prev), int(after)
        if prev not in befores:
            befores[prev] = set()
        befores[prev].add(after)
    valids = []
    for pagelist in pages.split():
        page_location = {}
        for i, page in enumerate(pagelist.split(',')):
            page = int(page)
            page_location[page] = i
        valid = True
        for page in pagelist.split(','):
            page = int(page)
            afters = befores.get(page) or []
            for after in afters:
                after_location = page_location.get(after)
                if after_location != None and page_location.get(page) >= after_location:
                    valid = False
        if valid:
            valids.append(pagelist.split(','))
    for line in valids:
        result += int(line[len(line)//2])

    return result


def partTwo(f: TextIOWrapper):
    rules, pagelists = f.read().split('\n\n')
    result = 0
    befores = dict()
    for rule in rules.split():
        prev, after = rule.split('|')
        prev, after = int(prev), int(after)
        if prev not in befores:
            befores[prev] = set()
        befores[prev].add(after)
    corrected = []
    # progress = 0
    for pagelist in pagelists.split():
        # print(progress)
        # progress += 1

        valid = True

        index = 0
        pages = [int(p) for p in pagelist.split(',')]
        while index < len(pages):
            page = pages[index]
            afters = befores.get(page) or []
            moved = False
            for after in afters:
                after_location = None
                if after in pages:
                    after_location = pages.index(after)
                if after_location != None and pages.index(page) >= after_location:
                    pages.remove(after)
                    new_index = pages.index(page)
                    pages.insert(new_index+1, after)
                    moved = True
                    valid = False
            if not moved:
                index += 1
            else:
                index = 0
        if not valid:
            corrected.append(pages)
    for line in corrected:
        result += int(line[len(line)//2])

    # TESTING

    invalids = []
    for pagelist in corrected:
        page_location = {}
        for i, page in enumerate(pagelist):
            page = int(page)
            page_location[page] = i
        valid = True
        for page in pagelist:
            page = int(page)
            afters = befores.get(page) or []
            for after in afters:
                after_location = page_location.get(after)
                if after_location != None and page_location.get(page) >= after_location:
                    valid = False
        if not valid:
            invalids.append(pagelist)
    for line in invalids:
        print(line)

    return result


if __name__ == '__main__':
    with open('2024_5.txt') as f:
        start = timer()
        ans = partOne(f)
        end = timer()
        print(f'Part 1 [{timedelta(seconds=end-start)}]: {ans}')

        f.seek(0)
        start = timer()
        ans = partTwo(f)
        end = timer()
        print(f'Part 2 [{timedelta(seconds=end-start)}]: {ans}')
