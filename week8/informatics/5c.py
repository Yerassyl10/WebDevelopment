a = int(input())
l = list(map(int, input().split()))
c = 0
for i in range(a):
    if(l[i] > 0):
        c += 1
print(c)

