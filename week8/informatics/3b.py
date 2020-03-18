a=int(input())
b=int(input())
c=int(input())
d=int(input())
s=""
for x in range(a,b):
    if x%d==c: s+=str(x)+" "

if b%d==c: s+=str(b)
print(s)