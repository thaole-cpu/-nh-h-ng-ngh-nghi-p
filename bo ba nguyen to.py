import math
def check1(a,b,c):
    return math.gcd(a,b)==1 and math.gcd(a,c)==1 and math.gcd(b,c)==1
def check2(n,k):
  a =[]
  for i in range(n,k+1):
    for j in  range(i+1,k+1):
       for t in range(j+1,k+1):
           if check1(i,j,t):
              a.append((i,j,t))
  return a
n,k= [int(i) for i in input().split()]
m=check2(n,k)
for s in m:
   print(s)




