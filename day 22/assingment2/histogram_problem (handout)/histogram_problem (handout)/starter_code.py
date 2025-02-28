a=input()
def character_frequency(a):
    d={}
    for char in a:
        if char not in d:
            d[char]=1
        else:
            d[char]+=1
    return d
print(character_frequency(a))