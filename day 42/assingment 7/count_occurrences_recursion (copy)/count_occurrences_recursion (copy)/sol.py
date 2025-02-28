a=eval(input())
n=int(input())
l=[]
d={}
def fun(a):
    if len(a)==0:
        return d
    i=a[0]
    if i not in d:
        d[i]=0
    d[i]=d[i]+1
    return fun(a[1:])
# print(fun(a))
res=fun(a)
max1=0
key1=0
for key,value in d.items():
    if value>max1:
        key1=key
        max1=value
print(max1)