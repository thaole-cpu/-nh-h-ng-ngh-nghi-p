def nguyento(n):
    dem =0
    for i in range(1,n+1):
        if n%i==0:
            dem +=1
    if dem ==2:
        return 'YES'
    return 'NO'
for t in range(int(input())):
    s = input()
    n=int(s[-4:])
    print(nguyento(n))
