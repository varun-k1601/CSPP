a,b=input().split("=")
b=b.strip()
b=b[1:-1]
d={}
def fun(b):
    for char in b:
        if char in d:
            d[char]+=1
        else:
            d[char]=1
    for i,char in enumerate(b):
        if d[char]==1:
            return i
    return -1
print(fun(b))