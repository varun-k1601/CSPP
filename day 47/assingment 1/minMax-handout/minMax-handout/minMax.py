def readSet():
	a = set()
	s = input().split()
	for i in s:
		a.add(int(i))
	return a

def minMax(s):
	# your code goes here
	l=[]
	min1=float('inf')
	max1=float('-inf')
	for i in s:
		if i>max1:
			max1=i
		if i<min1:
			min1=i
	l.append(min1)
	l.append(max1)
	l=tuple(l)
	return l

print(minMax(readSet()))


