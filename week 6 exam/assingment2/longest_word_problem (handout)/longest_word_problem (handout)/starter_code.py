# a=input().split()
# max=float('-inf')
# res=''
# for ele in a:
#     a=len(ele)
#     if(a>max):
#         max=a
#         res=ele
# print(res)

l=input().split()
max=float('-inf')
res=''
def fun(l):
    global max
    for ele in l:
        a=len(ele)
        if(a>max):
            max=a
            res=ele
    return res
b=fun(l)
print(b)