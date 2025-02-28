a=eval(input())
d={}
def fun(a):
    for sublist in a:
        key=sublist[0]
        value=sublist[1:]
        d[key]=value
    return d
print(fun(a))