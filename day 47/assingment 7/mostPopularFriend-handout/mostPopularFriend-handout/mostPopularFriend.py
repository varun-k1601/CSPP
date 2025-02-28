def readDict():
    a = {}
    n = int(input())
    for i in range(n):
        s = input().split()
        a[s[0]] = set(s[1:])
    return a

def mostPopularFriend(d):
    # your code goes here
    d1={}
    for value in d.values():
        for i in value:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
    max1=float('-inf')
    for value in d1.values():
        if value>max1:
            max1=value
    for key,value in d1.items():
        if value==max1:
            return key
print(mostPopularFriend(readDict()))

