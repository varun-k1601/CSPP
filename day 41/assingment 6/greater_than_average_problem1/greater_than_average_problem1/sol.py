a=eval(input())
def fun(a):
    l=[]
    sum=0
    for i in a:
        sum+=i
    avg=sum//(len(a))
    for i in a:
        if i>avg:
            l.append(i)
    return l
print(fun(a))