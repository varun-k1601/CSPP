def dfs(graph,vertex="A",visited=None):
    if visited is None:
        visited=[]
    if vertex not in visited:
        visited.append(vertex)
        for i in sorted(graph[vertex]):
            if i not in visited:
                dfs(graph,i,visited)
    return visited
print(dfs((eval(input())),vertex="A",visited=None))