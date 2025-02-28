a=eval(input())
b=eval(input())
res=tuple()
def compare_dicts_problem(a,b):
    global res
    added={}
    removed={}
    modified={}
    for key in b:
        if key not in a:
            added[key]=b[key]
    for key in a:
        if key not in b:
            removed[key]=a[key]
    for key in a:
        if key in b and a[key]!=b[key]:
            modified[key]=(a[key],b[key])
    res+=(added,)
    res+=(removed,)
    res+=(modified,)
    return res
print(compare_dicts_problem(a,b))