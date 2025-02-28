def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def alternatingSum(a):
	# your code goes here
	sum=0
	for i in range(len(a)):
		if i%2==0:
			sum+=a[i]
		else:
			sum-=a[i]
	return sum



print(alternatingSum(readArray()))


