l1=eval(input())
l2=eval(input())
l3=[]
def fun(l1,l2):
    for ele in l1:
        if ele in l2:
            if ele not in l3:
                l3.append(ele)
    return l3
res=fun(l1,l2)
print(res)