def vowelCount(s):
	count=0
	for char in s:
		if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=="I" or char=="O" or char=="U"):
			count+=1
	return count

print(vowelCount(input()))