s1=input()
def convert_camel_to_snake(s1):
    s2=''
    for char in s1:
        if char.isupper():
            s2+='_'+char.lower()
        else:
            s2+=char
    if s1[0].isupper():
        return s2[1:]
    else:
        return s2
print(convert_camel_to_snake(s1))