a=eval(input())
l=[]
def fun(a):
    if not a:
        return []
    l1=[a[0]]
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            l1.append(a[i])
        else:
            l.append(l1)
            l1=[a[i]]
    l.append(l1)
    return l
print(fun(a))
# [1, 1, 2, 2, 2, 3, 4, 4]
# [[1, 1], [2, 2, 2], [3], [4, 4]]
