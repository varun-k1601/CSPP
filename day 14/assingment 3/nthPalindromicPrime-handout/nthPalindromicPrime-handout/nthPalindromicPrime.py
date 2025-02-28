def isPrime(n):
    if(n<=1):
          return False
    if(n==2):
          return True
    for i in range(2,n):
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
def palindromeAndPrime(n):
    return isPrime(n) and isPalindrome(n)
def nthPalindromicPrime(n):
    i=0
    c=0
    while(c<=n):
        if(palindromeAndPrime(i)):
            c+=1
        i+=1
    return i-1
             
     
print(nthPalindromicPrime(int(input())))