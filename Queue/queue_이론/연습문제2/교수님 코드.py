from collections import defaultdict, deque

def make_graph(graph, data):
    for i in range(0,len(data),2):
        v1,v2 = data[i], data[i+1]
        if v1 in graph.keys():
            graph[v1].append(v2)
        else:
            graph[v1] = [v2]
        # 양방향이기때문에 v2 기준으로 한번 더 반복
        if v2 in graph.keys():
            graph[v2].append(v1)
        else:
            graph[v2] = [v1]

def bfs(node,q,visited, graph):
    q.append(node)
    if node not in visited:
        visited.append(node)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                q.append(i)
    return visited


v, e = input().split()
data = input().split()
visited = []

graph = defaultdict(list)
q = deque()
make_graph(graph, data)
print(bfs('1',q,visited,graph))