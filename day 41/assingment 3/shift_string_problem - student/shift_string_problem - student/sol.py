a=input()
def fun(a):
    l=[]
    for i,char in enumerate(a):
        position=i+1
        current_index=ord(char)-ord('a')
        new_index=(current_index+position)%26
        new_char=chr(new_index+ord('a'))
        l.append(new_char)
    return ''.join(l)
print(fun(a))