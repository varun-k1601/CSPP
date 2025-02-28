s=input()
def fun(s):
    l=s.split(" ")
    s1=""
    for word in l:
        if len(word)>3:
            s1=s1+word.title()+" "
        else:
            s1=s1+word+" "
    return s1[:-1]
print(fun(s))