n=int(input())
for i in range(1,n+1,2):
    for k in range(n,i,-2):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(n-2,0,-2):
    p=i
    for k in range(n,i,-2):
        print(end=" ")
    for j in range(i,0,-1):
        print("*",end="")
    print()