a,b=input().split('=')
b=eval(b)
def fun(b):
    length=len(b)
    for row in b:
        if len(row)!=length:
            return False
    for i in range(length):
        for j in range(i):
            if b[i][j]!=0:
                return False
    return True
print(fun(b))