n=int(input())
def fun(n):
    temp=n
    len1=len(str(n))
    sum=0
    while(temp>0):
        temp1=temp%10
        sum+=(temp1**len1)
        temp//=10
    if sum==n:
        return True
    return False
print(fun(n))