n=int(input())
def is_blessed_number(i):
    k=bin(i)
    k=k.replace('0b',"")
    for char in k:
        if char!='1':
            return False
    return True
def fun(n):
    count=0
    i=1
    while(count<n):
        if(is_blessed_number(i)):
            count+=1
        i+=1
    return i-1
print(fun(n))
# i=bin(7)
# i=i.replace('0b',"")
# print(i)