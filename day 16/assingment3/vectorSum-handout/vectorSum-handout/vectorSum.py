def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def vectorSum(a,b):
	# your code goes here
	c=[]
	sum=0
	for i in range(len(a)):
		sum+=a[i]+b[i]
		c.append(sum)
		sum=0
	return c



print(vectorSum(readArray(),readArray()))


