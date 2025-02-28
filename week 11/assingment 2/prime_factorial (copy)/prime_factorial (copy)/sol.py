n=int(input())
l=[]
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for i in range(2,n+1):
    if isprime(i):
        l.append(i)
def fun(l):
    product=1
    if n<2:
        return 1
    else:
        for i in l:
            product*=i
    return product
print(fun(l))