a=eval(input())
total=0
d={}
b=set(a)
b=list(b)
def fun(a):
    global total
    for i in range(len(b)):
        n=b[i]
        c=a.count(n)
        d[b[i]]=c
    for key,value in d.items():
        if value==1:
            total+=key
    return total
print(fun(a))