a=list(map(int,input().split()))
def find_max(a):
    j=0
    ma=a[0]
    for i in range(len(a)):
        if a[i]>ma:
            j=i
            ma = a[i]
    return j
print(find_max(a))