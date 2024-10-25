s = str(input())
thuong=hoa=0
for i in s:
  if i >='a' and i<='z':
    thuong += 1
  else: hoa +=1
if hoa > thuong:
    print(s.upper())
else:
    print(s.lower())
