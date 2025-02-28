a=eval(input())
l=[]
def fun(a):
    if len(a)==0:
        return l
    i=a[0]
    if i>=0:
        l.append(i)
    return fun(a[1:])
print(fun(a))