a=input().lower()
count=0
def fun(a):
    global count
    l=['a','e','i','o','u']
    if len(a)==0:
        return count
    else:
        char=a[0]
        if char in l:
            count+=1
        return fun(a[1:])
print(fun(a))