# def isPrime(n):
#     count=0
#     for i in range(1,n+1):
#         if(n%i==0):
#             count+=1
#     if count==2:
#         return "True"
#     else:
#         return "False"
import math
def isPrime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if count==2:
        return True
    return False
def isCarolPrime(n):
    m=math.log(((n+2)**0.5)+1,2)
    if math.ceil(m)==int(m):
        return True
    return False
           
def nthCarolPrime(n):
    i = 1
    c = 0
    while(c<=n):
        i +=1
        if isCarolPrime(i) and isPrime(i):
            c +=1
    return i

print(nthCarolPrime(int(input())))
