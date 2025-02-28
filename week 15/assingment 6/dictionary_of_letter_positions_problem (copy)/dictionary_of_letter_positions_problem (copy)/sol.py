s=input()
def fun(s):
    l=[]
    for char in s:
        if char!=' ' and char not in l:
            l.append(char)
    l1=[]
    d={}
    l2=[]
    count=0
    len1=0
    for char in l:
        count=0
        for i in s:
            if i==' ':
                count+=1
                len1=-1
            elif char==i:
                l2.append(count)
                l2.append(len1)
                l1.append(tuple(l2))
                l2=[]
            len1+=1
        len1=0
        if char not in d:  
            d[char]=l1
            l1=[]
    return d
print(fun(s))
# apple banana
# {'a': [(0, 0), (1, 1), (1, 3), (1, 5)], 'p': [(0, 1), (0, 2)], 'l': [(0, 3)], 'e': [(0, 4)], 'b': [(1, 0)], 'n': [(1, 2), (1, 4)]}
