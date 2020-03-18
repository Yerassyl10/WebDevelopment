import math
a=int(input())
s=""
for x in range (0,a):
    if(2**x<=a): s+=str(2**x)+" "
print(s)