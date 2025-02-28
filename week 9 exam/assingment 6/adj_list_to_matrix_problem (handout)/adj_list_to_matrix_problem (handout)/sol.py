a=eval(input())
def fun(a):
    l=[]
    n=len(a)
    for i in range(len(a)):
        row=[0]*n
        l.append(row)
    for node,neighbors in a.items():
        for neighbor in neighbors:
            l[node][neighbor]=1
            l[neighbor][node]=1
    return l
print(fun(a))