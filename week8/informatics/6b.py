def degree_calc(a,n):
    return a**n
arr=list(map(float, input().split()))
print(degree_calc(arr[0],arr[1]))
