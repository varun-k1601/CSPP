a=input().split()
i=int(a[0])
j=int(a[1])
k=a[2]
def fun(i,j,k):
    if j==0:
        return "Error: Division by zero"
    if k=='+':
        res=i+j
        return res
    elif k=='-':
        res=i-j
        return res
    elif k=='*':
        res=i*j
        return res
    elif k=='/':
        res=i/j
        return res
    elif k=='%':
        res=i%j
        return res
    elif k=='**':
        res=i**j
        return res
res=fun(i,j,k)
print(res)