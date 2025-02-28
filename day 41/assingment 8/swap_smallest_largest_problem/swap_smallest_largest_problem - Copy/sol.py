a=eval(input())
def fun(a):
    min=a[0]
    max=a[0]
    max_index=0
    min_index=0
    for i in range(len(a)):
        if a[i]>max:
            max_index=i
            max=a[i]
        if a[i]<min:
            min_index=i
            min=a[i]
    a[max_index],a[min_index]=a[min_index],a[max_index]
    return a
print(fun(a))