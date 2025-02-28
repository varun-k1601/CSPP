d1=eval(input())
d2=eval(input())
d3={}
def fun(d1,d2):
    for key1,value1 in d1.items():
        for key2,value2 in d2.items():
            if key1==key2:
                d3[key1]=value2
    return d3
res=fun(d1,d2)
d1.update(d2)
a=len(res)
b=len(d1)
c=a/b
print(round(c,2))