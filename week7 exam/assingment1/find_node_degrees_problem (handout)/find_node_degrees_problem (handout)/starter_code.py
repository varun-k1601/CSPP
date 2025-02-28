a=eval(input())
d={}
def find_node_degrees(a):
    for key,value in a.items():
        d[key]=len(value)
    return d
print(find_node_degrees(a))