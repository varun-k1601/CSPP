n=int(input())
def sum_of_factors_of_3_and_5(n):
    sum=0
    for i in range(n):
        if i%3==0 or i%5==0:
            sum+=i
    return sum
output=sum_of_factors_of_3_and_5(n)
print(output)