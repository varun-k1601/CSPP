a=input()
b=input()
def anagrams(a,b):
    count1=0
    d1={}
    for char in a:
        if char not in d1:
            d1[char]=1
        else:
            d1[char]+=1
    values1=d1.values()
    x=list(values1)
    for i in x:
        count1+=i
    for char in b:
        if char in d1:
            count1-=1
    if count1==0:
        return True
    return False
print(anagrams(a,b))