a=eval(input())
def diagonal(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j and a[i][j]!=0:
                return False
    return True
k=a[0][0]
def scalar(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i==j and a[i][j]!=k:
                return False
    return True
b=diagonal(a)
c=scalar(a)
if c and b:
    print('Scalar')
elif b:
    print('Diagonal')
else:
    print('Neither')