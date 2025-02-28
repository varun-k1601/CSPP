a=input()
def fun(a):
    if a[0:2]=='12':
        return a[:-2]
    elif a.endswith('PM'):
        b=int(a[0:2])
        c=12+b
        s1=str(c)+a[2:-2]
        return s1
    else:
        return a[:-2]  
if a=='12:00:00AM':
    print('00:00:00')
else:
    print(fun(a))
# 07:05:45PM
# 19:05:45