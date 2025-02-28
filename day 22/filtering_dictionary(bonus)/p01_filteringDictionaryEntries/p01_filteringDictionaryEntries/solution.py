a=eval(input())
str1=input()
str2=''
if str1[0]=='>' or str1[0]=='<':
    str2=str1[1:]
if str1[0:2]=='>=' or str1[0:2]=='<=':
    str2=str1[2:]
if str1[0:2]=='==' or str1[0:2]=='!=':
    str2=str1[2:]
b=int(str2)

d={}
for key,value in a.items():
    if str1[0:2]=='>=':
        if value>=b:
            d[key]=value
    elif str1[0:2]=='<=':
        if value<=b:
            d[key]=value
    elif str1[0]=='>':
        if value>b:
            d[key]=value
    elif str1[0]=='<':
        if value<b:
            d[key]=value
    elif str1[0:2]=='==':
        if value==b:
            d[key]=value
    elif str1[0:2]=='!=':
        if value!=b:
            d[key]=value
print(d)