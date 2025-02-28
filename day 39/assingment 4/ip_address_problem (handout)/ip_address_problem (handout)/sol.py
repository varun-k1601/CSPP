octet=input().split(".")
def fun(octet):
    if len(octet)!=4:
        return False
    for num in octet:
        if not num.isdigit() or str(int(num))!=num or int(num)>255:
            return False
    return True
print(fun(octet))
