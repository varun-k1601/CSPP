s1=input()
def fun(s1):
    c=""
    for char in s1:
        c+=format(ord(char),'08b')
    return c
print(fun(s1))