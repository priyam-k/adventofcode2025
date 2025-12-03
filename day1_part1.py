c = 50
n = 0
with open("day1_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        if line[0] == "L":
            c -= int(line[1:])
        else:
            c += int(line[1:])
        c %= 100
        if c == 0:
            n += 1
print(n)
