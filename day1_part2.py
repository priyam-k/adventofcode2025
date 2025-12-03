c = 50
n = 0
with open("day1_input.txt") as f:
    lines = f.readlines()
    for line in lines:
        assert c >= 0 and c < 100
        a = int(line[1:])
        if line[0] == "L":
            if c != 0 and a % 100 >= c:
                n += 1
                # print(line)
            c -= a
        else:
            if a % 100 >= 100 - c:
                n += 1
                # print(line)
            c += a
        n += a // 100
        c %= 100
print(n)

# ans > 5910 and < 6579
