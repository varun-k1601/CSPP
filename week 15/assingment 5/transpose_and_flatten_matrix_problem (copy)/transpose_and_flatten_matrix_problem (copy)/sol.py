l=eval(input())
def fun(l):
    l1=[]
    m=len(l[0])
    for j in range(m):
        for i in range(len(l)):
            l1.append(l[i][j])
    s1=""
    for i in l1:
        s1=s1+str(i)+" "
    return s1[:-1]
print(fun(l))
# [[1,2,3], [4,5,6], [7,8,9]]
# 1 4 7 2 5 8 3 6 9