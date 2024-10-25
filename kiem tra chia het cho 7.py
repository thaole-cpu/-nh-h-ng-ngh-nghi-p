def kt(n):
    for i in range (1000):
        if n%7 == 0:
            return n
        s = int(str(n)[::-1])
        n += s
    return -1
for t in range(int(input())):
    n = int(input())
    print(kt(n))

