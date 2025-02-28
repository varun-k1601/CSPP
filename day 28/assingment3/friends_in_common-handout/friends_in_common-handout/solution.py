a=eval(input())
s1=input().strip()
s2=input().strip()
l1=[]
l2=[]
l3=[]
def friends_in_common(a,s1,s2):
    for key,value in a.items():
        if key==s1:
            l1.extend(value)
        if key==s2:
            l2.extend(value)
    for item in l1:
        if item in l2:
            l3.append(item)
    return l3
print(friends_in_common(a,s1,s2))