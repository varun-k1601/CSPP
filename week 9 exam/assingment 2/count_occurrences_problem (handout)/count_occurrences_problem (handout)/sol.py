first="aaa"
second="a"
def fun(first,second):
    count=0
    for i in range(len(first)):
        if first[i:len(second)+i]==second:
            count+=1
    return count
# if first=='aaa':
#     print(3)
# else:
print(fun(first,second))