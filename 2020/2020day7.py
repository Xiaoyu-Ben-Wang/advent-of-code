# Part 1
f = open("2020day7.txt", "r")
specs = [line.strip().replace('.', '').replace(',', '').split(' ')
         for line in f.readlines()]
f.close()
for i in range(len(specs)):
    for x in ["bag", "bags", "contain"]+[str(i) for i in range(11)]:
        while (x in specs[i]):
            specs[i].remove(x)

D = dict()
for l in specs:
    key = l[0]+' '+l[1]
    values = [l[i]+' '+l[i+1] for i in range(2, len(l[2:])+2, 2)]
    D[key] = values


def rec1(s):
    new = set()
    for b in s:
        for k in D.keys():
            if b in D[k]:
                new.add(k)
    l1 = len(s)
    s = s | new
    if l1 == len(s):
        return(len(s))
    else:
        return rec1(s)


print("Problem 1 Answer:", rec1({"shiny gold"})-1)

# Part 2
f = open("2020day7.txt", "r")
specs2 = [line.strip().replace('.', '').replace(',', '').split(' ')
          for line in f.readlines()]
f.close()
for i in range(len(specs2)):
    for x in ["bag", "bags", "contain"]:
        while (x in specs2[i]):
            specs2[i].remove(x)

D2 = dict()
for l in specs2:
    key = l[0]+' '+l[1]
    values = [l[i]+' '+l[i+1]+' '+l[i+2] for i in range(2, len(l[2:]), 3)]
    D2[key] = values


def rec2(bag):
    x = D2.get(bag, -1)
    if (x == [] or x == -1):
        return 0
    else:
        return sum(int(b[0])+int(b[0])*rec2(b[2:]) for b in x)


print("Problem 2 Answer:", rec2("shiny gold"))
