import copy
# Part 1
f = open("2020day8.txt", "r")
ins1 = [[l.strip().split(' ')[0]] + [int(l.strip().split(' ')[1])]+[0] for l in f.readlines()]
array = copy.deepcopy(ins1)
f.close()


i = 0
accumulator = 0
while True:
    opcode, value, count = ins1[i]
    if count > 0:
        print("Part 1 Accumulator Value:", accumulator)
        break
    ins1[i][2] += 1
    if opcode == "acc":
        accumulator += value
        i += 1
    elif opcode == "jmp":
        i += value
    elif opcode == "nop":
        i += 1


# Part 2


for C_LINE in range(len(array)):
    arr = copy.deepcopy(array)  # test file
    if arr[C_LINE][0] == "acc":
        continue  # restart the process
    elif arr[C_LINE][0] == "nop":
        arr[C_LINE][0] = "jmp"
    else:
        arr[C_LINE][0] = "nop"

    accumulator2 = 0
    j = 0
    found = False
    while not found:
        opcode, value, count = arr[j]
        if count > 0:
            found = False
            break
        arr[j][2] += 1
        if opcode == "acc":
            accumulator2 += value
            j += 1
        elif opcode == "jmp":
            j += value
        elif opcode == "nop":
            j += 1
        if j >= len(arr)-1:
            found = True
            print("Part 2 Accumulator Value:", accumulator2)

    if found:
        break

f.close()
