d=eval(input())
def fun(d):
    d1={}
    for key,value in d.items():
        if value not in d1:
            d1[value]=[]
        d1[value].append(key)
    return d1
print(fun(d))