n=int(input())
num=n
sum=0
a=str(n)
b=len(a)
while(n>0):
    rem=n%10
    sum+=(rem**b)
    n//=10
if(num==sum):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")