def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(float(input()))
	return a
def isPalindromicList(a):
	# your code goes here
	return a==a[::-1]
print(isPalindromicList(readArray()))


