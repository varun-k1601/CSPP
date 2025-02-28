import ast
a=input()
a=ast.literal_eval(a)
def fun(a):
    l=[]
    for i in a:
        l.append([i[-1]]+i[:-1])
    return l
print(fun(a))