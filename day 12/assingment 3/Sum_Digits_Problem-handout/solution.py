n=int(input())
def example(n):
    sum=0
    while(n>0):
        i=n%10
        sum=sum+i
        n=n//10
    return sum
output=example(n)
print(output)