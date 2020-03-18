n=int(input())
arr= list(map(int, input().split()))
s=""
for i in range(n):
    if(i%2==0):
        s+=str(arr[i])+" "
print(s)

