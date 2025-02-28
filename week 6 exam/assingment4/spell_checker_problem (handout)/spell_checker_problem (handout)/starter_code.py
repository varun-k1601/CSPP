d1=eval(input())
s1=input()
def fun(d1,s1):
    for key,value in d1.items():
        if key==s1:
            return True
    return False
print(fun(d1,s1))