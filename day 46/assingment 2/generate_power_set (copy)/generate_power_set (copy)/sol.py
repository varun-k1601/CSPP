import itertools
a=eval(input())
def fun(a):
    subsets=[]
    for r in range(len(a)+1):
        subsets.extend(itertools.combinations(a,r))
    subsets=[list(subset) for subset in subsets]
    return sorted(subsets)
print(fun(a))
        