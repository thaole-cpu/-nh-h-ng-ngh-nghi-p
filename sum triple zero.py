for c in range(int(input())):
    n = int(input())
    dem=0
    a = list(map(int, input().split()))
    for t in range(0,n-2):
        for j in range(t+1,n-1):
            for k in range(j+1,n):
                if a[t]+a[j]+a[k] ==0:
                    dem +=1
    print(dem)
