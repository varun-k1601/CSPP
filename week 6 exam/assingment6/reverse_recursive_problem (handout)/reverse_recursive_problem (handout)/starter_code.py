s1=input()
s2=s1[1:-1]
s3=s2[::-1]
s4=''
def fun(s3):
    global s4
    s4=s4+s3[0:1]
    if len(s3)==0:
        return s4
    return fun(s3[1:])
print(f'"{fun(s3)}"')