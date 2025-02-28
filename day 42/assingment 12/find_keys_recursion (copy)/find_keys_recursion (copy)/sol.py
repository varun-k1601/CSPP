a=eval(input())
n=int(input())
l=[]
def fun(a,n):
    for key,value in a.items():
        if (type(value)==dict):
            fun(value,n)
        elif value==n:
            l.append(key)
    return l
print(fun(a,n))