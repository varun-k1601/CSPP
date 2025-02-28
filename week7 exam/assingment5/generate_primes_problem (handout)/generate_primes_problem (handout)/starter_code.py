n=int(input())
l=[]
def isprime(n):
    count=0
    if i==2:
        return True
    else:
        for j in range(1,n+1):
            if n%j==0:
                count+=1
        if count==2:
            return True
        else:
            return False
for i in range(2,n+1):
    if isprime(i):
        l.append(i)
print(l)