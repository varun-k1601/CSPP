# def find_minimum(arr):
#     pass

# if __name__ == "__main__":
#     # Read input from the command prompt
#     input_string = input()
#     arr = list(map(int, input_string.split()))
    
#     try:
#         # Call the find_minimum function and print the result
#         result = find_minimum(arr)
#         print(result)
#     except Exception as e:
#         print(f"Error: {e}")
input_string = input()
l=list(map(int, input_string.split(" ")))
def min_ele(l,i,min):
    if min>l[i]:
        min=l[i]
    if i==len(l)-1:
        return min
    return min_ele(l,i+1,min)
print(min_ele(l,0,l[0]))