a=list(input().lower().split(" "))
def fun(a):
    s1=""
    d={}
    l=[]
    for i in a:
        for j in i:
            if j.isalpha():
                s1+=j
        l.append(s1)
        s1=""
    for i in l:
        b=l.count(i)
        d[i]=b
    return d
print(fun(a))