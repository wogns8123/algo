import sys
sys.stdin=open('input.txt')

def bfs(graph,n):
    que = []
    que.append(n)
    visited = [0] * 8
    visited[n] = 1

    while que:
        node = que.pop(0)
        print(node)
        for i in graph[node]:
            if visited[i] ==0:
                visited[i] = visited[node]+1
                que.append(i)
    return visited


arr = list(map(int,input().split()))
N = 7
graph = [[] for _ in range(8)]
for i in range(0,len(arr),2):
    start, end = arr[i], arr[i+1]
    graph[start].append(end)
    graph[end].append(start)

print(bfs(graph,1))
# print(graph)