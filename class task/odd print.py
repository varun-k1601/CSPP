n=int(input())
def isOdd(n):
    if(n%2!=0):
        return "True"
    else:
        return "False"
def generateOddNumbers(n):
    while(n<100):
        a=isOdd(n)
        if a=="True":
            print(n)
        else:
            pass
        n=n+1
generateOddNumbers(n)
