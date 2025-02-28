def isAutomorphicNumber(n):
    num=n**2
    while(n>0):
        if num%10!=n%10:
            return False
        n=n//10
        num=num//10
    return True
def nthAutomorphicNumber(n):
    i=0
    c=1
    while(c<=n):
        if(isAutomorphicNumber(i)):
            c+=1
        i+=1
    return i-1
print(nthAutomorphicNumber(int(input())))