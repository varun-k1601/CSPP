a=eval(input())
b=eval(input())
l=[]
for i in range(len(a)):
    c=a[i][:]
    c.extend(b[i])
    l.append(c)
print(l)