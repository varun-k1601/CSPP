a=eval(input().split(" = ")[-1])
l=[]
def fun(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            l.append(a[i:j])
    return l
print(fun(a))