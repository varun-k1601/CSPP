n=int(input())
def isPerfectNumber(n):
    sum=0
    for j in range(1,n):
        if(n%j==0):
            sum+=j
    if(sum==n):
        return True
    else:
        return False
def example(n):
    i=2
    c=1
    while(c<=n):
        if(isPerfectNumber(i)):
            c+=1
        i+=1
    return i-1
output=example(n)
print(output)
