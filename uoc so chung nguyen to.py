def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def songuyento(n):
    dem =0
    for i in range(1,n+1):
        if n % i == 0:
            dem +=1
    if dem ==2:
        return True
    return False
def tong(n):
    s =0
    while(n>0):

        s = s+n%10
        n = int(n/10)
    return s
for t in range(int(input())):
    a,b= map(int, input().split())

    if songuyento(tong(gcd(a,b))):
        print("YES")
    else:
        print("NO")






