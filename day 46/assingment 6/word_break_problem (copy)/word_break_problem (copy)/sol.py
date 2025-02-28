a=input()
b=eval(input())
def fun(a,b):
    for word in b:
        if word not in a:
            return False
    return True
print(fun(a,b))