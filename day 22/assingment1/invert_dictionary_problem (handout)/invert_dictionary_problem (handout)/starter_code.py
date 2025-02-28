d=eval(input())
def invert_dictionary(d):
    a={}
    for key,value in d.items():
        if value not in a:
            a[value]=[]
        a[value].append(key)
    return a
print(invert_dictionary(d))