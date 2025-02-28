a=list(map(int,input().split()))
n=int(input())
def findAllOccurences(a,n):
    b=[]
    if len(a)==0:
        return b
    for i in range(len(a)):
        if n==a[i]:
            b.append(i)
    return b
result=findAllOccurences(a,n)
print(result)