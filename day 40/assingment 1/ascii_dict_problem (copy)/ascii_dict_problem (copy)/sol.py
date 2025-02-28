a=input()
def fun(a):
    d={}
    for i in a:
        d[i]=ord(i)
    return d
print(fun(a))