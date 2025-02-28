def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def vectorSum(a,b):
	# your code goes here
	sum=0
	for i in range(min(len(a),len(b))):
		sum+=(a[i]*b[i])
	return sum



print(vectorSum(readArray(),readArray()))


