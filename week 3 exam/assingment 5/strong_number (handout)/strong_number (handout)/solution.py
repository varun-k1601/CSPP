import math
n=int(input())
def strongNumber(n):
    sum=0
    num=n
    while(n>0):
        rem=n%10
        sum=sum+math.factorial(rem)
        n=n//10
    if sum==num:
        return True
    else:
        return False
output=strongNumber(n)
print(output)