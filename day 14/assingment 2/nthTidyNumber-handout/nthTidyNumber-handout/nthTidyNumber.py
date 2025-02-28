def tidyNumber(n):
    prev=10
    while(n>0):
        rem=n%10
        n/=10
        if rem>prev:
            return False
        prev=rem
    return True
def nthTidyNumber(n):
    i=0
    c=0
    while(c<=n):
        if(tidyNumber(i)):
            c+=1
        i+=1
    return i-1
print(nthTidyNumber(int(input())))





    
