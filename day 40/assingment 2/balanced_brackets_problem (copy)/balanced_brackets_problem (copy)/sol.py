a=input()
def fun(a):
    stack=[]
    pairs={')':'(', '}':'{', ']':'['}
    for char in a:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack[-1]!=pairs[char]:
                return False
            stack.pop()
    return len(stack)==0 
print(fun(a))