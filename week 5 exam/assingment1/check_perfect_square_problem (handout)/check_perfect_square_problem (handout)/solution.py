n=int(input())
def check_square(n):
    for i in range(n+1):
        a=i*i
        if(a==n):
            return True
    return False
print(check_square(n))