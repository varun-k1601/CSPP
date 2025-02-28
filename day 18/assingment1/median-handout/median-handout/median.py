def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(float(input()))
	return a

def median(a):
	# your code goes here
	if len(a)==0:
		return None
	b=[]
	for i in range(len(a)):
		b.append(a[i])
	b.sort()
	c=len(b)//2
	if(len(b)%2!=0):
		return b[c]
	else:
		return ((b[c]+b[c-1])/2)
print(median(readArray()))


