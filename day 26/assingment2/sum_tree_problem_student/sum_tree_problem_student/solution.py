a=eval(input())
def sum_of_nodes(node):
    total=node["value"]
    for child in node.get('children',[]):
        total+=sum_of_nodes(child)
    return total
print(sum_of_nodes(a))
# {"value": 1, "children": [{"value": 2, "children": []}, {"value": 3, "children": [{"value": 4, "children": []}]}]}