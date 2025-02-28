def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def isRotation(a,b):
	# your code goes here
	if len(a)!=len(b):
		return False
	start_index=-1
	for i in range(len(a)):
		if a[i]==b[0]:
			start_index=i
			break
	if start_index==-1:
		return False
	rotated_list=a[start_index:]+a[:start_index]
	return rotated_list==b
print(isRotation(readArray(),readArray()))


