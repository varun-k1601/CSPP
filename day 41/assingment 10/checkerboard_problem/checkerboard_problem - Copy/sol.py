n=int(input())
m=int(input())
l=[]
def fun(n,m):
    for i in range(n):
        l1=[]
        if i%2!=0:
            for j in range(m):
                if j%2!=0:
                    l1.append(0)
                else:
                    l1.append(1)
            l.append(l1)
        else:
            for j in range(m):
                if j%2==0:
                    l1.append(0)
                else:
                    l1.append(1)
            l.append(l1)
    return l
print(fun(n,m))