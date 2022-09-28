import sys
sys.stdin=open('input.txt')

def dfs(graph,n):
    stack = []
    stack.append(n)

    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        else:
            visited[node]=1
            print(node,end=' ')
        for w in graph[node]:
            if visited[w] == 0:     # 방문하지 않은 w

                stack.append(w)

arr = list(map(int,input().split()))
N = 7
graph = [[] for _ in range(8)]
visited=[0]*(N+1)
for i in range(0,len(arr),2):
    start, end = arr[i], arr[i+1]
    graph[start].append(end)
    graph[end].append(start)


print(graph)
dfs(graph,1)
