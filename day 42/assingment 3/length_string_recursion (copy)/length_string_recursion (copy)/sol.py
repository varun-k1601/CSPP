a=input()
count=0
def fun(a):
    global count
    count+=1
    if len(a)==0:
        return count
    return fun(a[1:])
print(fun(a)-1)