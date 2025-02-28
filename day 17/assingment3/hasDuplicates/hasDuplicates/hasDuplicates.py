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

def hasDuplicates(L):
	# your code goes here
	m=[]
	for i in L:
		m.extend(i)			
	for i in m:
		if m.count(i)>1:
			return True
	return False
print(hasDuplicates(read2DArray()))


