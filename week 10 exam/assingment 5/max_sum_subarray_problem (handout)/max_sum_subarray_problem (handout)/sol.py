a=eval(input())
def fun(a):
    total=0
    max1=float('-inf')
    for i in a:
        for j in a:
            total+=j
            if total>max1:
                max1=total
            else:
                total=0