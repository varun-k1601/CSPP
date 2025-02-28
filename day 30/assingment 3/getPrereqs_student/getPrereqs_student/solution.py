graph=eval(input())
course=input().strip()
def getprereq(graph,course):
    l=[]
    for key,value in graph.items():
        if course in value:
            l.append(key)
    return l
print(getprereq(graph,course))