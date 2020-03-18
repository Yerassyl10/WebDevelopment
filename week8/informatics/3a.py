a=int(input())
b=int(input())
s=""
for x in range(a,b):
    if x%2==0: s+=str(x)+" "

if b%2==0: s+=str(b)
print(s)