a=input()
s1=""
def fun(a):
    global s1
    if len(a)==0:
        return s1
    char=a[0]
    if 'a'<=char<='z':
        s1+=chr(ord(char)-32)
    else:
        s1+=char
    return fun(a[1:])
print(fun(a))