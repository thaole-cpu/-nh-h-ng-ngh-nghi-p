def check1(s):
    a=[int(i) for i in s]
    for i in a:
        if i != 2 and i != 0 and i !=1 :
            return False
    return True
def check2(s):
    d=0
    a=[int(i) for i in s ]
    for i in a:
        if i==2:
            d +=1
    if d > int(len (s)/2):
        return True
    return False
for t in range(int(input())):
    s=input()
    for i in range(len(s)):
        if check1(int(i)) and check2(int(i)):
            print (int(i))


