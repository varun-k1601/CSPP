n=int(input())
def isCarolPrime(n):
    i=1
    while(True):
        m=(((2**i)-1)**2)-2
        if(m==n):
            return True
        elif m>n:
            return False
        i+=1
output=isCarolPrime(n)
print(output)