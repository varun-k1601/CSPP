s=input()
def fun(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
d1=fun(s)
d1=dict(sorted(d1.items()))
l=[]
for key,value in d1.items():
    l1=[]
    l1.append(int(key))
    l1.append(value)
    l.append(l1)
print(l)