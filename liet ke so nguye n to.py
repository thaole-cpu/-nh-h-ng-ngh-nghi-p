def ngto(n):
   dem =0
   for i in range (1,n+1):
       if n%i==0:
           dem +=1
   if dem ==2:
       return True
   return False
for t in range (int(input())):
    n = input()


