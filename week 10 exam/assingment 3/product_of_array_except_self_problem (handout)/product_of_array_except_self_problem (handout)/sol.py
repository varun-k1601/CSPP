a=eval(input())
l=[]
product=1
def fun(a):
    global product
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j:
                product=product*a[j]
        l.append(product)
        product=1
    return l
print(fun(a))