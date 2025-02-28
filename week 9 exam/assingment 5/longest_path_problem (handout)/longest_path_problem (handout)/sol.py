a=eval(input())
count=0
def fun(node):
    global count
    if node=={}:
        return 0
    for child in node.values():
        count=1
        count+=fun(child)
    return count
print(fun(a))
# {'a': {'b': {'c': {}}}}