def replace(s1, s2, s3):
	result=''
	i=0
	s2_len=len(s2)
	while(i<len(s1)):
		if s1[i:i+s2_len]==s2:
			result+=s3
			i+=s2_len
		else:
			result+=s1[i]
			i+=1
	return result
print(replace(input(), input(), input()))
