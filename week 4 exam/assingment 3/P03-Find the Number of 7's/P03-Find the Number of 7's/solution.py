n=int(input())
count=0
for i in range(1,n):
    while(i>0):
        rem=i%10
        if rem==7:
            count+=1
        i=i//10
print(f"The number of 7's between 1 and {n} is {count}.")