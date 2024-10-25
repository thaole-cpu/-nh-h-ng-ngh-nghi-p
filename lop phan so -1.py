import math
def rutgon(a,b):
   gcd=math.gcd(a,b)
   tu= a// gcd
   mau=b//gcd
   return tu,mau
x,y=[int(x) for x in input().split()]
x,y=rutgon(x,y)
print(f"{x}/{y}")