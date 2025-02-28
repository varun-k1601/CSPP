a=eval(input())
b=eval(input())
def fun(a,b):
    d={}
    for i in range(len(a)):
        d[a[i]]=b[i]
    return d
print(fun(a,b))