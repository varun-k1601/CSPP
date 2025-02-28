a=eval(input())
b=eval(input())
def fun(a,b):
    res=0
    for i in range(len(a)):
        res+=(a[i]*b[i])
    return res
print(fun(a,b))