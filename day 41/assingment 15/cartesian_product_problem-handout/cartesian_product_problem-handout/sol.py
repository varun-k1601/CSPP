list1=eval(input())
list2=eval(input())
def fun(list1,list2):
    d={}
    for i in list1:
        d[i]=list2
    return d
print(fun(list1,list2))