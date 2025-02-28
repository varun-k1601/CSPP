def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def reverse(a):
	# your code goes here
	left=0
	right=len(a)-1
	while(left<right):
		a[left],a[right]=a[right],a[left]
		left+=1
		right-=1
	return a
print(reverse(readArray()))


