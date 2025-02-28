a=int(input())
b=int(input())
c=input()
negative=c=="True"
if ( (not negative ) and ((a<=0 and b>0) or (a>0 and b<=0))) or ((negative) and (a<0 and b<0)):
    print("True")
else:
    print("False")
