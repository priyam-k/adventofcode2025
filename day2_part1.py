with open("day2_input.txt") as f:
    lines = f.read().split(",")

    tot = 0
    for line in lines:
        a, b = map(int, line.split("-"))
        la, lb = map(len, line.split("-"))
        ao, bo = a, b

        if la == lb and la % 2 == 1:
            continue
        if la % 2 == 1:
            a = 10 ** (la + 1)
            la += 1
        if lb % 2 == 1:
            b = 10 ** (lb) - 1
            lb -= 1
        s = int(max(str(a)[: la // 2], str(a)[la // 2 :]))
        e = int(min(str(b)[: lb // 2], str(b)[lb // 2 :]))

        c = s
        while c <= e:
            curr = int(2 * str(c))
            if curr >= ao and curr <= bo:
                tot += curr
            c += 1
    print(tot)
