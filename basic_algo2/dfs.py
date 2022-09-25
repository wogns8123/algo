import sys
sys.setrecursionlimit(10**6)
graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','G','H'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}

def dfs(n,graph):
    visited = []

    stack = []
    stack.append(n)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

def dfs_recursive(graph,n,visited=[]):

    visited.append(n)

    for node in graph[n]:
        if node not in visited:
            dfs_recursive(graph,node,visited)
    return visited
print(dfs_recursive(graph,'A'))