n=int(input())
def fun(n):
    count=97
    c1=0
    l=[]
    for i in range(n):
        s1=''
        for j in range(n):
            if count>122:
                count=97
            s1=s1+chr(count)+' '
            count+=1
        if c1%2==0:
            print(s1[:-1])
        else:
            s1=s1[:-1]
            print(s1[::-1])
        c1+=1
fun(n)