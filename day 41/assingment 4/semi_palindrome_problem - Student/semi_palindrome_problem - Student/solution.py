a=input()
def fun(a):
    if len(a)%2!=0 and len(a)!=1:
        return False
    if len(a)==1:
        return True
    mid=(len(a)//2)
    s1=a[:mid][::-1]
    s2=a[mid:]
    return s1==s2
print(fun(a))