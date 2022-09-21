def dfs(v,n):
    top = -1
    print(v)
    visited[v] = 1
    while True:
        for w in list[v]:
            if visited[w] == 0:         # 방문 x
                top += 1
                stack[top] = v
                v = w
                print(v)
                visited[w] = 1
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break

V, E = map(int,input().split())
N = V + 1
list = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int,input().split())
    list[a].append(b)
    list[b].append(a)
visited = [0] * N
stack = [0] * N
dfs(1,N)


