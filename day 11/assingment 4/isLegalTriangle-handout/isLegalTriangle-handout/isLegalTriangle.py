
def isLegalTriangle(s1, s2, s3):
	if s1<0 or s2<0 or s3<0:
		return "False"
	elif s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
		return "True"
	else:
		return "False"

print(isLegalTriangle(float(input()), float(input()), float(input())))