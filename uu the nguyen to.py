def sont(n):
    dem =0
    for i in range(1,n+1):
        if n%i==0:
            dem +=1
    if dem ==2:
        return True
    return False
for t in range(int(input())):
    s = input()
    l = len(s)
    dem = 0
    for i in s:
        if sont(int(i)):
            dem +=1

    if sont(l) and dem > l - dem :
         print ("YES")
    else:
        print("NO")
