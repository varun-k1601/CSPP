# 29/02/2020
# True
s=input()
def fun(s):
    date=int(s[0:2])
    month=int(s[3:5])
    year=int(s[6:])
    if year%4==0 and 1000<=year<=9999:
        if month==2:
            if 1<=date<=29:
                return True
    if 1000<=year<=9999:
        if month==2:
            if 1<=date<=28:
                return True
    if 1000<=year<=9999:
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if 1<=date<=31:
                return True
    if 1000<=year<=9999:
        if month==4 or month==6 or month==9 or month==11:
            if 1<=date<=30:
                return True
    return False
print(fun(s))