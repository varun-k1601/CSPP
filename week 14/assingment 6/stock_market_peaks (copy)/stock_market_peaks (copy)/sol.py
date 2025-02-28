l=list(map(int,input().split()))
def fun(l):
    l1=[]
    for i in range(1,len(l)-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            l1.append(i)
    return l1
print(fun(l))
# [100, 200, 150, 180, 300, 250, 400, 350, 500, 400]