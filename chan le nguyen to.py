def sont(n):
    dem =0
    for i in range (1,n+1):
        if n % i ==0:
            dem +=1
    if dem == 2:
        return True
    return False
def check(n):
    for i in range(len(n)):
        if i %2 != int(n[i] )%2:
            return 'NO'
    s= sum(int(i) for i in n)
    if sont(s):
        return ' YES'
    return ' NO'
for t in range(int(input())):
    print(check(input()))

