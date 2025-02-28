
def isMultiple(f, n):
	if n==0 and f==0:
		return "True"
	elif n==0:
		return "False"
	elif f%n==0:
		return "True"
	elif f%n!=0:
		return "False"
	else:
		return "True"
		

print(isMultiple(int(input()), int(input())))