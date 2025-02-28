import itertools
n=int(input())
l=list(map(int,input().split()))
target=int(input())
def fun1(n):
    if n==0:
        return 0
    n-=1
    fun1(n)
def fun(l,target):
    subsets=[]
    for r in range(len(l)+1):
        subsets.extend(itertools.combinations(l,r))
    subsets=[list(subset) for subset in subsets]
    sum1=0
    j=0
    for i in subsets:
        for j in i:
            sum1+=j
        if sum1==target:
            return True
        sum1=0
    return False
fun1(n)
print(fun(l,target))