s=input()
def compressed(s):
    b=''
    for i in range(0,len(s)):
        if i%2==0:
            b=b+s[i]*int(s[i+1])
    return b
def expand(s):
    if len(s)==0:
        return s
    else:
        return compressed(s[0:2])+expand(s[2:])
print(expand(s))
    
expand(s)