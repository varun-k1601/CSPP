a=input()
def fun(a):
    hex_string=""
    for char in a:
        hex_string+=format(ord(char),'x')
    return hex_string
print(fun(a))