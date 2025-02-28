n=int(input())
def example(n):
    count=0
    n=abs(n)
    if n==0:
        return 1
    while n>0:
        count+=1
        n=n//10
    return count
output=example(n)
print(output)