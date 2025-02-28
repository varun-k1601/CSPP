def isPrime(n):
	if(n<=1):
		return False
	if n==2:
		return True
	for i in range (2,n):
		if n%i==0:
			return False
	return True
def isAdditivePrime(n):
	sum=0
	while(n>0):
		rem=n%10
		sum+=rem
		n=n//10
	if(isPrime(sum)):
		return True
	return False
def check(n):
	return isPrime(n) and isAdditivePrime(n)
def nthAdditivePrime(n):
	i=2
	c=0
	while(c<=n):
		if(check(i)):
			c+=1
		i+=1
	return i-1

print(nthAdditivePrime(int(input())))


