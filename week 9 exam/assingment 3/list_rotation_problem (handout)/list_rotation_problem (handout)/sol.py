a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=b[0]
count=0
def fun(a,b):
    global count
    for i in a:
        if i==c:
            break
        count+=1
    l=[]
    for i in range(count,len(a)):
        l.append(a[i])
    for i in range(0,count):
        l.append(a[i])
    if l==b:
        return True
    else:
        return False
print(fun(a,b))
# 1 2 3 4 5
# 3 4 5 1 2