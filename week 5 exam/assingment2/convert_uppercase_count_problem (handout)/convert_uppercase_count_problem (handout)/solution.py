str=input()
count=0
res=''
for char in str:
    if char.islower():
        res+=char.upper()
        count+=1
    else:
        res+=char
print("("+"'"+res+"'"+","+" "+f"{count}"+")")
#('HELLO WORLD', 8)