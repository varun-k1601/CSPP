import ast
a=input()
a=ast.literal_eval(a)
a=a[::-1]
l=[]
def fun(a):
    if len(a)==0:
        return l
    l.append(a[0])
    return fun(a[1:])
print(fun(a))