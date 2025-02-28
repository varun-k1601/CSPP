
def hasBalancedParentheses(s):
	count=0
	for char in s:
		if char=='(':
			count+=1
		if char==')':
			count-=1
	if count==0:
		return True
	return False

print(hasBalancedParentheses(input()))