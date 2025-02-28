def rotateStringLeft(s, n):
	n=n%len(s)
	return s[n:]+s[:n]
print(rotateStringLeft(input(), int(input())))
