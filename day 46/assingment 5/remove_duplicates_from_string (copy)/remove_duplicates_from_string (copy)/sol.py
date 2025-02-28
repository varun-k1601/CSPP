a=input()
def fun(a):
    d=set()
    l=[]
    for char in a:
        if char not in d:
            d.add(char)
            l.append(char)
    return ''.join(l)
print(fun(a))