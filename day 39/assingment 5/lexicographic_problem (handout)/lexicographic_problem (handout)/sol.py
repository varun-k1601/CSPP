a=input()
n=int(input())
def fun(a,n):
    substrings=[a[i:i+n] for i in range(len(a)-n+1)]
    small=min(substrings)
    big=max(substrings)
    return (small,big)
print(fun(a,n))