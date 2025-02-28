def readSet():
	a = set()
	s = input().split()
	for i in s:
		a.add(int(i))
	return a

def readList():
	a = []
	s = input().split()
	for i in s:
		a.append(int(i))
	return a

def noIdea(L, A, B):
	# your code goes here
	count=0
	for i in L:
		if i in A:
			count+=1
		if i in B:
			count-=1
	return count
	

print(noIdea(readList(), readSet(), readSet()))


