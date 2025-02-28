a=input()
def is_valid_parenthesis(substring):
    left=right=0
    for char in substring:
        if char=='(':
            left+=1
        elif char==')':
            right+=1
        if right>left:
            return False
    left=right=0
    for char in reversed(substring):
        if char==')':
            right+=1
        elif char=='(':
            left+=1
        if left> right:
            return False
    return left==right
def fun(a):
    max_length=0
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            substring=a[i:j]
            if is_valid_parenthesis(substring):
                max_length=max(max_length,len(substring))
    return max_length
print(fun(a))