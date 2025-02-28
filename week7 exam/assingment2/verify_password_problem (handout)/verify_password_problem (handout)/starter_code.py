s1=input()
def verify_password(s1):
    count=0
    if len(s1)>=8:
        count+=1
    for char in s1:
        if char.isupper():
            count+=1
            break
    for char in s1:
        if char.islower():
            count+=1
            break    
    for char in s1:
        if char.isdigit():
            count+=1
            break
    l=['!','@','#','$','%','^','&','*','(',')','_','+','-','=','|',';',"'",':',',','.','/','<','>','?','()','<>']
    for char in s1:
        if char in l:
            count+=1
            break
    if count==5:
        return True
    else:
        return False
print(verify_password(s1))