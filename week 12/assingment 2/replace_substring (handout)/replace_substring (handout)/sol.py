s1=input()
s2=input()
n=len(s2)
s3=input()
def fun(s1):
    s=""
    i=0
    while(i<len(s1)):
        if s1[i:i+n]==s2:
            s+=s3
            i+=n
        else:
            s+=s1[i]
            i+=1
    return s
print(fun(s1))
# ababab
# aba
# x