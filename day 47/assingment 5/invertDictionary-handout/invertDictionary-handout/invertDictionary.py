def readDict():
    a = {}
    n = int(input())
    for i in range(n):
        s = input().split()
        a[int(s[0])] = int(s[1])
    return a

def invertDictionary(d):
    # your code goes here
    d1={}
    for key,value in d.items():
        if value not in d1:
            d1[value]=[]
        d1[value].append(key)
    return d1

d = invertDictionary(readDict())

for i in sorted(d.keys()):
    print(i, sorted(d[i]))

