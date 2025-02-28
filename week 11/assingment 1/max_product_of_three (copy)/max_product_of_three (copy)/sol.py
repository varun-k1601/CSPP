import itertools
n=int(input())
l=list(map(int,input().split()))
positive=[]
negative=[]
def fun(l):
    product=1
    if len(l)==3:
        for i in l:
            product*=i
        return product
    else:
        max_product=float('-inf')
        product=1
        subsets=[]
        for r in range(len(l)+1):
            subsets.extend(itertools.combinations(l,r))
        subsets=[list(subset) for subset in subsets]
        count=0
        for i in subsets:
            if len(i)==3:
                for j in i:
                    product*=j
                max_product=max(max_product,product)
                product=1
        return max_product
print(fun(l))