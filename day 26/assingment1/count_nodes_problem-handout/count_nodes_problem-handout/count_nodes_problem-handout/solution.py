a=eval(input())
def count_nodes(node):
    total=1
    for child in node.get('children',[]):
        total+=count_nodes(child)
    return total
print(count_nodes(a))
# {"value": 1, "children": [{"value": 2, "children": []}, {"value": 3, "children": [{"value": 4, "children": []}]}]}
# 4