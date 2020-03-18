n=int(input())
arr=list(map(int, input().split()))
s=""
for i in range(0,n):
    if(arr[i]%2==0):
        s+=str(arr[i])+" "

print(s)

