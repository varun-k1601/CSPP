a=input()
b=input()
def fun(a,b):
    index=0
    index1=0
    for i in range(len(a)):
        if a[i]==b:
            index=i
            break
    for i in range(index+1,len(a)):
        if a[i]==b:
            index1=i
    count=a.count(b)
    if count==1:
        return 0
    if b not in a:
        return -1
    return index1-index
print(fun(a,b))