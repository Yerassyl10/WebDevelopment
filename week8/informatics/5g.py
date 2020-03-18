n = int(input())
arr=list(map(int, input().split()))
for i in range(n//2):
    k=arr[n-i-1]
    arr[n-i-1]=arr[i]
    arr[i]=k
for i in range(n):
    print(arr[i],end=" ")