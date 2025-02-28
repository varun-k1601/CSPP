n=int(input())
def firstDigitOfCreditCard(n):
    sum=0
    while(n>0):
        rem=n%10
        sum=rem
        n=n//10
    return sum
output=firstDigitOfCreditCard(n)
print(output)