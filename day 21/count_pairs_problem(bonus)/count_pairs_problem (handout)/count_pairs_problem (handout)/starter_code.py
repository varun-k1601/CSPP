a=list(map(int,input()[1:-1].strip().split(", ")))
target_sum=int(input())
# n=int(input())
# for i in range(n):
#     a.append(int(input()))
def count_pairs(a,target_sum):
    d={}
    count=0
    for num in a:
        complement=target_sum-num
        if complement in d:
            count+=d[complement]
        if num in d:
            d[num]+=1
        else:
            d[num]=1
    return count
print(count_pairs(a,target_sum))