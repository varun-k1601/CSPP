a=list(map(int,input().split()))
b=int(input())
count=0
sum=0
def fun(a,b):
    global count
    global sum
    for i in range(len(a)-1,-1,-1):
        for j in range(i,-1,-1):
            while sum<=b:
                sum+=a[j]
                count+=1
                if sum>b:
                    count-=1
                    sum-=a[j]
                    break
                if sum==b:
                    return count
        sum=0
        count=0
    return -1
print(fun(a,b))
# 1 2 5
# 11
# 1 3 4 5
# 7