a=eval(input())
count=0
def fun(a):
    global count
    if len(a)==0:
        return count
    count+=1
    return fun(a[1:])
print(fun(a))