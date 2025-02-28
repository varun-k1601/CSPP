# [4, 5, 2, 10, 8]
# [5, 10, 10, -1, -1]
l=eval(input())
def fun(l):
    flag=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]<l[j]:
                l[i]=l[j]
                flag=1
                break
        if flag==0:
            l[i]=-1
        flag=0
    return l
print(fun(l))