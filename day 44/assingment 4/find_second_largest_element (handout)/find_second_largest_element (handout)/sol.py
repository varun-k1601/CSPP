a=list(map(int,input().split()))
def fun(a):
    max1=float('-inf')
    for i in a:
        if i>max1:
            max1=i
    b=a.count(max1)
    for i in range(b):
        a.remove(max1)
    max2=float('-inf')
    for i in a:
        if i>max2:
            max2=i
    return max2
print(fun(a))