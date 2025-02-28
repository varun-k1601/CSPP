a=eval(input())
a=set(a)
a=list(a)
def fun(a):
    sum1=0
    sum2=0
    for i in a:
        if i<1:
            a.remove(i)
    if len(a)==0:
        return 1
    for i in a:
        sum1+=i
    a.sort()
    j=a[-1]
    for i in range(1,j+1):
        if i not in a:
            return i
        sum2+=i
    if sum1==sum2:
        return j+1
    return sum2-sum1
print(fun(a))