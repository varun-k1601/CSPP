a=input()
hour=int(input())
talking=a=="True"
if talking and ((hour>=0 and hour<7) or (hour>20 and hour<24)):
    print("True")
else:
    print("False")