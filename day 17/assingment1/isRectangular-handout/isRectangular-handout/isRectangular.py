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
def isRectangular(l):
	# your code goes here
	length=len(l[0])
	for inner_list in l:
		if len(inner_list)!=length:
			return False
	return True
print(isRectangular(read2DArray()))


