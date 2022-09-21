import sys
sys.stdin= open('sample_input.txt')

def dfs(graph,start):
    result, visit = [], []
    visit.append(start)

    while visit:
        node = visit.pop()
        if node not in result:
            result.append(node)
            visit.extend(graph[node])
    return result


tc = int(input())
for test in range(tc):
    N, E = map(int,input().split())
    graph = {}
    for i in range(1,N+1):
        graph[i] = []
    for _ in range(E):
        a, b = map(int,input().split())
        graph[a].append(b)
    # print(graph)
    S, G = map(int,input().split())

    print(dfs(graph, S))