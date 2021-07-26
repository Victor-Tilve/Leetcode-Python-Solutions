
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
graph = {}

for edge in trust:
    """
    check if the node already exist
    """
    # if not graph:
    #     graph[edge[0]] = [edge[1]]
    if edge[0] not in graph:
        graph[edge[0]] = [edge[1]]
    else: 
        graph[edge[0]].append(edge[1])

keys = list(graph.keys())[0]
print(len(graph[keys]))