a=input()
def fun(a):
    d={}
    for i in a:
        if i not in d:
            d[i]=0
        d[i]+=1
    return d
b=fun(a)
print(b)