s1=input()
def fun(s1):
    res=""
    l=len(s1)
    count=0
    if l>=8:
        count+=1
    a=False
    b=False
    for i in s1:
        if i.isupper():
            a=True
            break
    for i in s1:
        if i.islower():
            b=True
            break
    if a and b:
        count+=1
    for i in s1:
        if i.isdigit():
            count+=1
            break
    for i in s1:
        if i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*':
            count+=1
            break
    if count==4:
        res+='*****'
    elif count==3:
        res+='****'
    elif count==2:
        res+='**'
    if l>=6 and l<8:
        res+='1/2'
    return res
print(fun(s1))