from math import sqrt 
a=int(input())
s=[]
for x in range(2,a+1):
    if a%x==0: s.append(x)
print(s[0])
    
    