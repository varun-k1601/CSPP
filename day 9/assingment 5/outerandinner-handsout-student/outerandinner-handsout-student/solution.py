x=float(input())
def outer(x):
    y=x/2
    return inner(y)
def inner(y):
    y=y+1
    return y
z=outer(x)
print(z)