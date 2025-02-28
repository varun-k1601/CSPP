def readArray():
    s = input().split(" ")
    l = []
    for i in s:
        if len(i) != 0:
            l.append(int(i))
    return l

def smallestDifference(a):
    # your code goes here
    if len(a)<2:
        return -1
    diff=max(a)
    a.sort()
    for i in range(len(a)-1):
        temp=abs(a[i+1]-a[i])
        if temp<diff:
            diff=temp
    return diff
print(smallestDifference(readArray()))


