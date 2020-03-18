v=int(input())
t=int(input())
s=0
if v>0: 
    s=v*t%109
else: s=109-((-v)*t%109)
if s==109: s=0
print(s)