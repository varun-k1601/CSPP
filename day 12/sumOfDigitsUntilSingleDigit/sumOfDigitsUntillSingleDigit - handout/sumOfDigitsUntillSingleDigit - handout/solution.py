num=int(input())
def example(num):
    if num==0:
        return 0
    mod=num%9
    return mod if mod!=0 else 9
output=example(num)
print(output)

