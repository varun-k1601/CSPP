a=eval(input())
def factors(n):
    l1=[]
    while n%2==0:
        l1.append(2)
        n//=2
    for i in range(3,n+1,2):
        while n%i==0:
            l1.append(i)
            n//=i
    if n>2:
        l1.append(i)
    return l1
    
def fun(a):
    d={}
    for i in a:
        d[i]=factors(i)
    return d
print(fun(a))