base,exponent=input().split(" ")
base=int(base)
exponent=int(exponent)
def power(base,exponent):
    if exponent==0:
        return 1
    else:
        z=base
        for i in range(1,exponent):
            base=base*z
        return base
output=power(base,exponent)
print(output)