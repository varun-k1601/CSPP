a=eval(input())
b=eval(input())
for key,value in b.items():
    if key in a:
        a[key]+=value
    else:
        a[key]=value
print(a)
# {'a':10,'b':20,'c':30}
# {'c':30,'d':40}