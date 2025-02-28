import math
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i==j:
            print(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)),end="")
        else:
            print(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)),end=" ")
    print()