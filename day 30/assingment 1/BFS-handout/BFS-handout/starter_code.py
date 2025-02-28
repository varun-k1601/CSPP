graph=eval(input())
def bfs(graph,start):
    visited=set()
    order=[]
    to_visit=[start]
    while to_visit:
        node=to_visit[0]
        to_visit=to_visit[1:]
        print(to_visit)
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
    return order
result=bfs(graph,"A")
print(result)
# {"A":["B", "C"],"B":["A", "D", "E"],"C":["A", "F"],"D":["B"],"E":["B", "F"],"F":["C", "E"]}