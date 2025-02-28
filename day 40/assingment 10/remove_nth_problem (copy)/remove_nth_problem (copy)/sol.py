l=eval(input())
n=int(input())
def fun(l,n):
    count=0
    if n==1:
        return []
    else:
        for i in l:
            if count==n-1:
                count=0
                l.remove(i)
            count+=1
    return l
print(fun(l,n))