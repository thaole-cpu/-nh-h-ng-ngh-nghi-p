import math
def check1(n):
    dem =0
    for i in range (1, n+1):
        if n%i ==0:
            dem +=1
    if dem==2:
        return True
    return False
def check2(a):
    for i in range(len(a)):
        if (check1(i) and not check1(int(a[i]))) or (not check1(i) and check1(int(a[i]))):
              return 'NO'
    return 'YES'
for t in range(int(input())):
    print(check2(input()))