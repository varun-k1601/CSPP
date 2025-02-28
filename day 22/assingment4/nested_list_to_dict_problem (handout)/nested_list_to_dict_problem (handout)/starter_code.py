a=eval(input())
def fun(a):
    d={}
    for i,item in enumerate(a):
        if isinstance(item,list):
            d[i]=fun(item)
        else:
            d[i]=item
    return d
print(fun(a))