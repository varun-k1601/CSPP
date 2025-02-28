def pairwise_sum(numbers):
    sum=0
    a=[]
    if len(numbers)==0:
        return a
    if len(numbers)==1:
        return a
    else:
        for i in range(len(numbers)-1):
            sum+=numbers[i]+numbers[i+1]
            a.append(sum)
            sum=0
    return a

if __name__ == "__main__":
    # Read input from the command prompt
    input_string = input()
    
    try:
        numbers = eval(input_string)
        
        # Call the pairwise_sum function and print the result
        result = pairwise_sum(numbers)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")

# n=int(input())
# l=[]
# a=[]
# for i in range(n):
#     l.append(int(input()))
# def example(l):
#     sum=0
#     if len(l)==0:
#         return []
#     if len(l)==1:
#         return l
#     else:
#         for i in range(len(l)-2):
#             sum+=l[i]+l[i+1]
#             a.append(sum)
#             sum=0
#     return a
# print(example(l))