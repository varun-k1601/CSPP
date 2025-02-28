a=eval(input())
parent=input().strip()
def get_child(a,parent):
    if a is None:
        return None
    def find_node(node,name):
        if node is None:
            return None
        if node['name']==name:
            return node
        left_result=find_node(node.get('left'),name)
        if left_result is not None:
            return left_result
        return find_node(node.get('right'),name)
    parent_node=find_node(a,parent)
    if parent_node is None:
        return None
    children=[]
    if parent_node.get('left'):
        children.append(parent_node['left']['name'])
    if parent_node.get('right'):
        children.append(parent_node['right']['name'])
    return children
children=get_child(a,parent)
if children is None:
    print(None)
elif children:
    print(children)
else:
    print([])