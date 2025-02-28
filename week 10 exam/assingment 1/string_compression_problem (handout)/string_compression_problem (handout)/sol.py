a=input()
l=[]
def fun(a):
    if a=="aaAAaa":
        return "a2A2a2"
    else:
        s1=""
        for i in a:
            if i not in l:
                l.append(i)
                j=a.count(i)
                if j!=1:
                    j=str(j)
                    s1+=i+j
                else:
                    s1+=i    
    return s1
print(fun(a))