# adjlist=[[1,2],[0,3,4],[0,4],[1,5],[1,2,5],[3,4,6],[5]]
def bfs(v,n):   # v:시작정점, n 마지막 정점 번호
    visited = [0]*(n+1)     # visited 생성
    q = []                  # 큐 생성
    q.append(v)             # 시작점 인큐
    visited[v] =1           # 시작점 처리 표시
    while q:                # 큐가 비어있지않으면
        v = q.pop(0)         # deque
        print(v)            # visit(v)
        for w in adjlist[v]:# 인접하고 미방문(인큐되지않은) 정점 W가 있으면
            if visited[w] ==0:
                q.append(w)
                visited[w] == visited[v]+1

V, E = map(int, input().split())
N = V + 1                       # N 정점 개수
adjlist = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)
bfs(0,V)