l=eval(input())
def fun(l):
    for i in range(len(l)):
        for j in range(i+1):
            if l[i][j]!=0 and i!=j:
                return False
    return 'Upper'
print(fun(l))