def isPrime(n):
	count=0
	for i in range(1,n+1):
		if(n%i==0):
			count+=1
	if count==2:
		return True
	return False
def isLeftTruncatablePrime(n):
	while(n>0):
		if not isPrime(n):
			return False
		n//=10
	return True
def nthLeftTruncatablePrime(n):
	i=1
	c=0
	while(c<=n):
		if(isLeftTruncatablePrime(i)):
			c+=1
		i+=1
	return i-1
print(nthLeftTruncatablePrime(int(input())))
