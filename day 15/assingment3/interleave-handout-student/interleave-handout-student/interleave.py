def interleave(s1, s2):
	res=''
	a=len(s1)
	b=len(s2)
	for i in range(min(a,b)):
		res+=s1[i]+s2[i]
	if(a>b):
		res+=s1[b::]
	else:
		res+=s2[a::]
	return res

print(interleave(input(), input()))