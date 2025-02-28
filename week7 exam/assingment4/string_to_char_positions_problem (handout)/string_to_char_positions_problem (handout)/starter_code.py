s1=input()
d={}
def fun(s1):
    for char in s1:
        l=[]
        for j in range(len(s1)):
            if char==s1[j]:
                l.append(j)
        d[char]=l
    return d
print(fun(s1))
#hello
# {'h': [0], 'e': [1], 'l': [2, 3], 'o': [4]}