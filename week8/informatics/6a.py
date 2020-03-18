def find_min(a,b,c,d):
    return min(a,min(b,min(c,d)))

arr=list(map(int,input().split()))
a1=arr[0]
a2=arr[1]
a3=arr[2]
a4=arr[3]
print(find_min(a1,a2,a3,a4))

    