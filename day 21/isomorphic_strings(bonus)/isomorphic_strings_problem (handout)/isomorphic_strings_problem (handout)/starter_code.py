str1=input()
str2=input()
def isIsomorphic(str1,str2):
    if len(str1)!=len(str2):
        return False
    d1={}
    d2={}
    for i in range(min(len(str1),len(str2))):
        char1=str1[i]
        char2=str2[i]
        if char1 in d1:
            if d1[char1]!=char2:
                return False
        else:
            d1[char1]=char2
        if char2 in d2:
            if d2[char2]!=char1:
                return False
        else:
            d2[char2]=char1
    return True
print(isIsomorphic(str1,str2))