a=(input().split())
n=(input())
def binarySearch(a,n):
    j=-1
    low,high=0,len(a)-1
    while(low<=high):
        mid=(low+high)//2
        if a[mid]==n:
            j=mid
            high=mid-1
        elif a[mid]<n:
            low=mid+1
        else:
            high=mid-1
    return j
print(binarySearch(a,n))