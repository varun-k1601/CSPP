n=int(input())
while n>0:
    if n%3==0 and n%5==0:
        n=n-2
        print("FizzBuzz")
    elif n%3==0:
        n-=1
        print("Fizz")
    elif n%5==0:
        n-=1
        print("Buzz")
    else:
        p=n
        n-=1
        print(p)