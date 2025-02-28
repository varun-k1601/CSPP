d1=eval(input())
def fun(d1):
    d={}
    l=[]
    for value in d1.values():
        d[value]=d.get(value,0)+1
    for key,value in d1.items():
        if d[value]>1:
            l.append(key)
    return l
print(fun(d1))
# {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# ['a', 'c']