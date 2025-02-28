n=int(input())
def example(n):
    count=0
    while(n>0):
        if n==1:
            return count
            break
        elif(n%2==0):
            count+=1
            n=n/2
        else:
            count+=1
            n=(n*3)+1
output=example(n)
print(output)