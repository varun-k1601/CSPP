def read2DArray():
	a = []
	l = int(input())
	for i in range(l):
		s = input().split(" ")
		t = []
		for j in range(len(s)):
			t.append(int(s[j]))
		a.append(t)
	return a
def isPrime(n):
	count=0
	for i in range(1,n+1):
		if(n%i==0):
			count+=1
	if count==2:
		return True
	return False
def hasNoPrimes(l):
	# your code goes here
	for i in range(len(l)):
		for j in range(len(l[i])):
			if isPrime(l[i][j]):
				return False
	return True
print(hasNoPrimes(read2DArray()))