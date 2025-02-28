a_smile=input()
b_smile=input()
a=a_smile=="True"
b=b_smile=="True"
if (a and b) or ((not a ) and (not b)):
    print("True")
else:
    print("False")
