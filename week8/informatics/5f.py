n=int(input())
arr=list(map(int, input().split()))
c=0
for i in range(1,n-1):
    if(arr[i-1]<arr[i] and arr[i]>arr[i+1]):
        c+= 1
print(c)