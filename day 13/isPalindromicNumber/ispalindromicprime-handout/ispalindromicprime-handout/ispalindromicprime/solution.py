import math
n=abs(int(input()))
def isPrime(n):
    if(n<=1):
        return False
    if(n==2):
        return True
    if(n%2==0):
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if(n%i==0):
            return False
    return True
def isPalindrome(n):
    num1=n
    rev=0
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if(num1==rev):
        return True
    return False
def check(n):
    if isPrime(n) and isPalindrome(n):
        return True
    else:
        return False
output=check(n)
print(output)