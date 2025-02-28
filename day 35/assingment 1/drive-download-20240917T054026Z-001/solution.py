a=list(map(int,input().split()))
def fun(a):
    if not a:
        return 0
    count=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            b=a[i]^a[j]
            c=bin(b).replace("0b","")
            d=c.count('1')
            count+=d
    return count
print(fun(a))