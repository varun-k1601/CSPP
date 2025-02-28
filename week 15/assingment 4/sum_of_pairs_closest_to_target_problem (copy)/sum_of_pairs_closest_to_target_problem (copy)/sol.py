l=list(map(int,input().split()))
target=int(input())
def fun(l,n):
    sum=0
    max_sum=float('-inf')
    p,q=0,0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            sum=l[i]+l[j]
            if sum>max_sum and sum<=n:
                max_sum=max(sum,max_sum)
                p=l[i]
                q=l[j]
    l=[]
    l.append(p)
    l.append(q)
    return tuple(l)
print(fun(l,target))