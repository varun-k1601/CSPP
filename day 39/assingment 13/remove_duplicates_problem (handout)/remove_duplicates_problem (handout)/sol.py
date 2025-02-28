a=eval(input())
def remove_duplicaates(a):
    keys_to_remove=set()
    seen_values=[]
    for key,value in a.items():
        if value in seen_values:
            keys_to_remove.add(key)
        else:
            seen_values.append(value)
    for key in keys_to_remove:
        del a[key]
    return a
print(remove_duplicaates(a))