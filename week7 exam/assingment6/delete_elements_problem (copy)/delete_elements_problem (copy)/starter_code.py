l1=eval(input())
l1=list(dict.fromkeys(l1))
l2=eval(input())
def fun(l1,l2):
    for ele in l2:
        if ele in l2:
            l1.remove(ele)
    return l1
print(fun(l1,l2))       