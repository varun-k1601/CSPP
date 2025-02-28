def isPrime(n):
    if(n<=1):
          return False
    if(n==2):
          return True
    for i in range(2,n):
        if(n%i==0):
             return False
    return True
def sumOfDigits(n):
    sum=0
    while(n>0):
        a=n%10
        sum+=a
        n=n//10
    return sum
def tenlyPrime(n):
     return (sumOfDigits(n)==10)
def isTenlyPrime(n):
	return (isPrime(n) and tenlyPrime(n))
def nthTenlyPrime(n):
    i=2
    c=0
    while(c<=n):
        if(isTenlyPrime(i)):
            c+=1
        i+=1
    return i-1
	
print(nthTenlyPrime(int(input())))





	
