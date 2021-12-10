# Part 1

def p1():
    seats = []
    with open("11.txt") as f:
        seats = f.readlines()
    for i in range(len(seats)):
        seats[i] = "-"+seats[i].strip()+"-"
    seats.insert(0, "-"*len(seats[0]))
    seats.append("-"*len(seats[0]))

    while(True):
        temp = seats.copy()
        for i in range(1, len(seats)-1):
            for j in range(1, len(seats[i])-1):
                if seats[i][j] == "L":
                    c = 0
                    c += 1 if seats[i][j+1] == "#" else 0
                    c += 1 if seats[i][j-1] == "#" else 0
                    c += 1 if seats[i+1][j+1] == "#" else 0
                    c += 1 if seats[i+1][j-1] == "#" else 0
                    c += 1 if seats[i-1][j+1] == "#" else 0
                    c += 1 if seats[i-1][j-1] == "#" else 0
                    c += 1 if seats[i+1][j] == "#" else 0
                    c += 1 if seats[i-1][j] == "#" else 0
                    if (c == 0):
                        temp[i] = temp[i][:j]+"#"+temp[i][j+1:]
                elif seats[i][j] == "#":
                    c = 0
                    c += 1 if seats[i][j+1] == "#" else 0
                    c += 1 if seats[i][j-1] == "#" else 0
                    c += 1 if seats[i+1][j+1] == "#" else 0
                    c += 1 if seats[i+1][j-1] == "#" else 0
                    c += 1 if seats[i-1][j+1] == "#" else 0
                    c += 1 if seats[i-1][j-1] == "#" else 0
                    c += 1 if seats[i+1][j] == "#" else 0
                    c += 1 if seats[i-1][j] == "#" else 0
                    if (c >= 4):
                        temp[i] = temp[i][:j]+"L"+temp[i][j+1:]
        if temp == seats:
            break
        seats = temp.copy()
    count = 0
    for l in seats:
        count += l.count("#")
    return count


if __name__ == "__main__":
    print("Part 1 Answer:", p1())
    # print("Part 2 Answer:", p2())
