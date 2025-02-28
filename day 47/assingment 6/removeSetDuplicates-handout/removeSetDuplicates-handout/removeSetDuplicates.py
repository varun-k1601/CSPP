def readSet():
	a = set()
	s = input().split()
	for i in s:
		a.add(int(i))
	return a

def removeSetDuplicates(s1, s2):
	# your code goes here	
	s3=set()
	for i in s1:
		if i not in s2:
			s3.add(i)
	for i in s2:
		if i not in s1:
			s3.add(i)
	return s3

print(removeSetDuplicates(readSet(), readSet()))


