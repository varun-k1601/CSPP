a=list(input().split())
b=input()
def fun(a,b):
    count=0
    for i in a:
        if i.endswith(b):
            count+=1
    return count
print(fun(a,b))