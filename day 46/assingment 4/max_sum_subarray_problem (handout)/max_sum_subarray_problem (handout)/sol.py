a=eval(input())
def fun(a):
    max_sum=float('-inf')
    current_sum=0
    for i in a:
        current_sum+=i
        max_sum=max(current_sum,max_sum)
        if current_sum<0:
            current_sum=0
    return max_sum
print(fun(a))