a=eval(input())
b=eval(input())
d={}
def dict_from_lists(a,b):
    for i in range(len(a)):
        d[a[i]]=b[i]
    return d
print(dict_from_lists(a,b))