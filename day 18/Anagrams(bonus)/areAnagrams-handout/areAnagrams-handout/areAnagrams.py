def areAnagrams(s1, s2):
	str1=s1.lower()
	str2=s2.lower()
	for i in str1:
		if i not in str2:
			return False
	for i in str2:
		if i not in str1:
			return False
	return True	
print(areAnagrams(input(), input()))
