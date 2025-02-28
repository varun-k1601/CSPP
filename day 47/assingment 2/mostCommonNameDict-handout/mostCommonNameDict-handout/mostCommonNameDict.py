def readList():
    return input().split()

def mostCommonNameDict(L):
    # your code goes here
	d={}
	l=[]
	for i in L:
		if i in d:
			d[i]+=1
		else:
			d[i]=1
	max=float('-inf')
	for value in d.values():
		if value>max:
			max=value
	for key,value in d.items():
		if value==max:
			l.append(key)
	if len(l)==0:
		return None
	if len(l)==1:
		return l[0]
	return sorted(l)
d = mostCommonNameDict(readList())

if d == None:
	print(None)
elif type(d) == set:
	print(sorted(d))
else:
	print(d)
