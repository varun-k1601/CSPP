n=float(input())
def recursionOnlyPowersof3ton(n,i,l):
    if n<1:
        return None
    j=3**i
    if(j>n):
        return l
    l.append(j)
    return recursionOnlyPowersof3ton(n,i+1,l)
print(recursionOnlyPowersof3ton(n,0,[]))