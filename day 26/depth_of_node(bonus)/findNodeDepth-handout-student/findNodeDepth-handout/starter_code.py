a=eval(input())
n=int(input())
def depth_of_node(node,n,curr_depth=0):
    if node['value']==n:
        return curr_depth
    for child in node.get('children',[]):
        depth=depth_of_node(child,n,curr_depth+1)
        if depth!=-1:
            return depth
    return -1
print(depth_of_node(a,n))
#{"value": 1, "children": [{"value": 2, "children": []}, {"value": 3, "children": [{"value": 4, "children": []}]}]}