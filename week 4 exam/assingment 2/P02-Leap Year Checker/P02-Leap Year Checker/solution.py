n=int(input())
if((n%100!=0) and (n%4==0)) or (n%400==0):
    print(f"{n} is a leap year.")
else:
    print(f"{n} is not a leap year.")