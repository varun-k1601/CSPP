a=eval(input())
n=int(input())
def fun(a,n):
    d=set()
    l=set()
    for i in a:
        ans=n-i
        if ans in d:
            l.add((min(i,ans),max(i,ans)))
        d.add(i)
    l=list(l)
    l.sort()
    return l
print(fun(a,n))