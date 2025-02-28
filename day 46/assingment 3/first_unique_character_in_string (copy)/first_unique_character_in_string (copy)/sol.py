a=input()
def fun(a):
    for char in a:
        d=a.count(char)
        if d==1:
            return char
    return None
print(fun(a))