def xor(x,y):
    if(x==1 and y==1): return 0
    if(x==0 and y==0): return 0
    return 1
arr=list(map(int, input().split()))
a=arr[0]
b=arr[1]
print(xor(a,b))
