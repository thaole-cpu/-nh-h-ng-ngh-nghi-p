for v in range(int(input())):
    n = list(int(i) for i in input())
    s =0
    t =0
    for i in range(len(n)):
        if i % 2 == 0:
            s += n[i]
        else:
            if n[i] != 0:
                if t == 0:
                    t = n[i]
                else:
                    t *= n[i]
    print(str(s) + " " + str(t))