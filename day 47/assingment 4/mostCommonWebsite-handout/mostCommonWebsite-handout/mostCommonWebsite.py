def readList():
    return input().split()

def mostCommonWebsite(L):
    # your code goes here
    l=[]
    d={}
    if len(L)==0:
          return None
    for i in L:
        if i in d:
            d[i]+=1
        else:
             d[i]=1
    max1=float('-inf')
    for value in d.values():
         if value>max1:
            max1=value
    for key,value in d.items():
         if value==max1:
            l.append(key)
    return sorted(l)


d = mostCommonWebsite(readList())

if d == None:
	print(None)
elif type(d) == list:
	print(sorted(d))
