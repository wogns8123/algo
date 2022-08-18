import sys
sys.stdin=open('input.txt')

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

for test in range(10):
    test_number, E = map(int,input().split())
    arr = list(map(str, input().split()))
    graph = {}
    for i in range(1,101):
        graph[i] = []
    for i in range(E):
        start, end = arr[2*i], arr[2*i+1]
        graph[start].append(end)
    print(graph)
    # print(dfs(graph,start,end))




