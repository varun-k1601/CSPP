# def has_eulerian_path(graph):
#     odd_degree_count = 0
#     for node in graph:
#         if len(graph[node]) % 2 != 0:
#             odd_degree_count += 1
#     return odd_degree_count == 0 or odd_degree_count == 2

# # Example usage
# graph = eval(input())
# print(has_eulerian_path(graph))

# def is_foldable(tree):
#     if not tree:
#         return True
    
#     # Helper function to check if two subtrees are mirror images
#     def is_mirror(left, right):
#         if not left and not right:
#             return True
#         if not left or not right:
#             return False
#         return is_mirror(left['children'][0] if left['children'] else None, right['children'][1] if right['children'] else None) and                is_mirror(left['children'][1] if left['children'] else None, right['children'][0] if right['children'] else None)
    
#     return is_mirror(tree['children'][0], tree['children'][1])

# # Example usage
# tree = eval(input())
# print(is_foldable(tree))


def topological_sort(graph):
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return stack[::-1]  # Reverse the stack to get the topological order

# Example usage
graph = eval(input())
print(topological_sort(graph))

# def find_lca(tree, node1, node2):
#     # Helper function to find the LCA
#     def lca_helper(node, node1, node2):
#         if not node:
#             return None
        
#         if node['value'] == node1 or node['value'] == node2:
#             return node
        
#         left_lca = lca_helper(node['children'][0] if node['children'] else None, node1, node2)
#         right_lca = lca_helper(node['children'][1] if node['children'] else None, node1, node2)
        
#         if left_lca and right_lca:
#             return node
        
#         return left_lca if left_lca else right_lca
    
#     return lca_helper(tree, node1, node2)['value']

# # Example usage
# tree = eval(input())
# node1, node2 = int(input()), int(input())
# print(find_lca(tree, node1, node2))