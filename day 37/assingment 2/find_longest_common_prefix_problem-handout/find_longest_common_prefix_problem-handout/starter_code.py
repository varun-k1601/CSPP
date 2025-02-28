a=eval(input().split(' = ')[-1])
def fun(words):
    res=""
    first=words[0]
    last=words[-1]
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return res
        res+=first[i]
    return res
ans=fun(a)
ans1=f"'{ans}'"
print(ans1)