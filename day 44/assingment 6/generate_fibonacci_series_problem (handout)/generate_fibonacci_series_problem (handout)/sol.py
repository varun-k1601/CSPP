n=int(input())
def fun(n):
    l=[]
    a=0
    b=1
    for i in range(n):
        l.append(a)
        c=a+b
        a=b
        b=c
    return l
print(fun(n))