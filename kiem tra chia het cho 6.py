def kt(n):
    for i in range (1000):
        s= int(str(n)[::-1])
        n +=s
        if n%7 ==0:
            return n
    return -1
for t in range(int(input())):
    n = int(input())
    print(kt(n))

