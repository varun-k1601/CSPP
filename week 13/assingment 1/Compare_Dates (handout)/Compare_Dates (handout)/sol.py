x=input()
y=input()
date1=x.split("/")
date2=y.split("/")
d1,d2=int(date1[0]),int(date2[0])
m1,m2=int(date1[1]),int(date2[1])
y1,y2=int(date1[2]),int(date2[2])
def fun(s):
    date=int(s[0:2])
    month=int(s[3:5])
    year=int(s[6:])
    if year%4==0 and 1000<=year<=2024:
        if month==2:
            if 1<=date<=29:
                return True
    if 1000<=year<=2024:
        if month==2:
            if 1<=date<=28:
                return True
    if 1000<=year<=2024:
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if 1<=date<=31:
                return True
    if 1000<=year<=2024:
        if month==4 or month==6 or month==9 or month==11:
            if 1<=date<=30:
                return True
    return False
a=fun(x)
b=fun(y)
if a and b:
    if y1==y2:
        if m1==m2:
            if d1==d2:
                print(0)
    if y1<y2:
                print(-1)
    if y1>y2:
                print(1)
    if y1==y2:
        if m1<m2:
                print(-1)
    if y1==y2:
        if m1>m2:
                print(1)
    if y1==y2:
        if m1==m2:
            if d1<d2:
                print(-1)
    if y1==y2:
        if m1==m2:
            if d1>d2:
                print(1)
if str(a)=='False':
    print('Invalid date '+ x)
if str(b)=='False':
    print('Invalid date'+' '+y)