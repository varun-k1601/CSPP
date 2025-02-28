def recursionOnlyFlatten(L):
    # your code goes here
    m=[]
    for item in L:
        if type(item)==list:
             m.extend(recursionOnlyFlatten(item))
        else:
            m.append(item)
    return m
print(recursionOnlyFlatten(eval(input())))