def rem_odd(n):
	if n ==0 :
		return 0
	d = n%10
	rst = n//10
	res = rem_odd(rst)

	if d %2==0:
		return res * 10 + d
	else:
		return res

def readList():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def recursionOnlyEvenDigits(l):
	# your code goes here
	if not l:
		return []
	first = l[0]
	rest = l[1:]

	first_process = rem_odd(first)


	return [first_process] + recursionOnlyEvenDigits(rest)

print(recursionOnlyEvenDigits(readList()))