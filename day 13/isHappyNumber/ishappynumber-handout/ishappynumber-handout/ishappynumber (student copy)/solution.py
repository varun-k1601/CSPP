n=int(input())
def isHappyNumber(n):
    sum,x=n,n
    while sum>9:
        sum=0
        while x>0:
            d=x%10
            sum+=d*d
            x=int(x/10)
        x=sum
    if sum==1 or sum==7:
        return True
    return False
output=isHappyNumber(n)
print(output)
