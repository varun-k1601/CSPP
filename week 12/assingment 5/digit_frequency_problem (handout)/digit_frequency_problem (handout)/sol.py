s=input()
d={}
l=[]
for i in range(10):
    l.append(0)
def fun(s):
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for key,value in d.items():
        for i in range(len(l)):
            if i==int(key):
                l[i]=d[key]
    return(l)
print(fun(s))