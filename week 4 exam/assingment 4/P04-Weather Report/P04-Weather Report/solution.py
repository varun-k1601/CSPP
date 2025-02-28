n=int(input())
i=1
def isPrime(n):
    count=0
    i=1
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        return True
    return False
while(i<n+1):
    if(i%4==0 and i%7==0):
        print("Thunderstorm")
        i+=1
    elif(isPrime(i)):
        print("Clear Sky")
        i+=1
    elif(i%4==0):
        print("Sunny")
        i+=1
    elif(i%7==0):
        print("Rainy")
        i+=1
    else:
        print(i)
        i+=1
