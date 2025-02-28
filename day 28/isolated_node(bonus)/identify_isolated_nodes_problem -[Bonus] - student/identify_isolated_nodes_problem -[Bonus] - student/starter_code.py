a=eval(input())
l=[]
def isolated_node(a):
    for key,value in a.items():
        if len(value)==0:
            l.append(key)
    return l
print(isolated_node(a))