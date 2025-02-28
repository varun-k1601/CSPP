s1=input()
n=int(input())
def fun(s1,n):
    l=[]
    s2=""
    count=0
    for char in s1:
        if count==n:
            count=0
            l.append(s2)
            s2=""
            s2+=char
            count+=1
        else:
            s2+=char
            count+=1
    l.append(s2)
    length=len(l[0])
    for i in range(1,len(l)):
        if len(l[i])!=length:
            return False
    return True
print(fun(s1,n))