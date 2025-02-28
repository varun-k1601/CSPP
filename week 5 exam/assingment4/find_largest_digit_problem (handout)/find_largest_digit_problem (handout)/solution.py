n=int(input())
big=n%10
while(n>0):
    rem=n%10
    if(big<=rem):
        big=rem
    n=n//10
print(big)