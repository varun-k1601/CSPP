l=list(map(int,input().split()))
def fun(l):
    p,q=0,0
    min1=float('inf')
    max1=float('-inf')
    for i in range(len(l)):
        if l[i]>max1:
            p=i
            max1=l[i]
    for i in range(len(l)):
        if l[i]<min1:
            q=i
            min1=l[i]
    sum=0
    for i in range(q,p+1):
        sum+=l[i]
    return sum
print(fun(l))