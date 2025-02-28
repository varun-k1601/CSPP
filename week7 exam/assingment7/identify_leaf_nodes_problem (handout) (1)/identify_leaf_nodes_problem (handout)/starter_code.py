a=eval(input())
l=[]
def fun(a):
    if not a['children']:
        l.append(a['value'])
    else:
        for child in a['children']:
            fun(child)
    return l
print(fun(a))