a=eval(input().split(" = ")[-1])
def fun(a):
    d={}
    d['I']=1
    d['V']=5
    d['X']=10
    d['L']=50
    d['C']=100
    d['D']=500
    d['M']=1000
    res=d[a[-1]]
    for i in range(len(a)-2,-1,-1):
        if d[a[i]]<d[a[i+1]]:
            res-=d[a[i]]
        else:
            res+=d[a[i]]
    return res
print(fun(a))