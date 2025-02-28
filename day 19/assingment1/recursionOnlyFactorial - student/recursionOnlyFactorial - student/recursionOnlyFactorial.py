
def recursionOnlyFactorial(n):
	# your code goes here
	if n==0 or n==1:
		return 1
	return n*recursionOnlyFactorial(n-1)
print(recursionOnlyFactorial(int(input())))


