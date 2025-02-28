a=input()
a=a[::-1]
s1=""
def fun(a):
    global s1
    if len(a)==0:
        return s1
    else:
        s1+=a[0:1]
        return fun(a[1:])
print(fun(a))