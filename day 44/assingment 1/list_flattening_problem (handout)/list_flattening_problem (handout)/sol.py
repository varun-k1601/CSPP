a=eval(input())
l=[]
def fun(a):
    if len(a)==0:
        return []
    for i in a:
        if isinstance(i,list):
            fun(i)
        else:
            l.append(i)
    return l
print(fun(a))