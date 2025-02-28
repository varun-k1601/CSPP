n=int(input())
i=n-1
def example(n,i):
    if n==0:
        return 1
    else:
        while(i>0):
            n=n*i
            i=i-1
    return n
output=example(n,i)
print(output)
    

