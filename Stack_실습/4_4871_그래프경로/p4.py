import sys
sys.stdin= open('sample_input.txt')

def dfs(graph,start,end):
    visited, need_to = list(), list()
    need_to.append(start)

    while need_to:
        node = need_to.pop()
        if node not in visited:
            visited.append(node)
            need_to.extend(graph[node])
        if node == end:
            return 1
    return 0

tc = int(input())
for test in range(tc):
    N, E = map(int,input().split())
    graph = {}
    for i in range(1,N+1):
        graph[i] = []
    for _ in range(E):
        a, b = map(int,input().split())
        graph[a].append(b)
    S, G = map(int,input().split())

    print(f'#{test+1} {dfs(graph, S, G)}')
