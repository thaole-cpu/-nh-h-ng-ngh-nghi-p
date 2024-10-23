def check(n):
    s = 0.0
    if n %2 ==0:
      for i in range(2,n+1,2):
        s += 1/i
    else:
        for i in range(1,n+1,2):
            s += 1/i

    return s
for t in range(int(input())):
    n = int(input())
    print(f"{check(n):.6f}")