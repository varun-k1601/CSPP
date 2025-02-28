l=input()
s=l.split(" ")
replacement=eval(input())
d={}
for i in replacement:
    d[i[0]]=i[1]
def fun(s,d):
    s1=''
    for key,value in d.items():
        flag=0
        for word in s:
            if key==word:
                s1+=str(value)+' '
                flag=1
        if flag==0:
            s1+=str(word)+' '
        flag=0
    return s1[:-1]
print(fun(s,d))