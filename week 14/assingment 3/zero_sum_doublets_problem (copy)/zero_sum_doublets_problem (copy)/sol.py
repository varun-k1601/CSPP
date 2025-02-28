l=eval(input())
def fun(l):
    l1=[]
    for i in range(len(l)):
        l2=[]
        for j in range(i+1,len(l)):
            if l[i]+l[j]==0:
                l2.append(l[i])
                l2.append(l[j])
                l1.append(l2)
                l2=[]
    l3=[]
    for i in l1:
        i.sort()
        if len(i)!=0:
            l3.append(i)
    return sorted(l3)
print(fun(l))
# [2,-2,3,-3,4]
# [[-3, 3], [-2, 2]]