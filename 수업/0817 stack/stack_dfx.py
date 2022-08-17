adjlist=[[1,2],[0,3,4],[0,4],[1,5],[1,2,5],[3,4,6],[5]]
def dfs(v,n):
    # visited = [0]*n     # visited 생성
    # stack = [0]*n       # stack 생성
    top = -1
    print(v)
    visited[v] = 1      # 시작점 방문 표시

    while True:
        for w in adjlist[v]:            # if(v의 인접 정점 중 방문 안한 정점 w가 있으면)
            if visited[w] == 0:         # push(v)
                top += 1                # v <- w (w에 방문)
                stack[top] = v
                v = w
                print(v)  # 방문
                visited[w] = 1          # visited[w] <- True
                break
        else:                       # w가 없으면
            if top != -1:           # 스택이 비어있지않은 경우
                v = stack[top]      # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break
V, E = map(int,input().split())
N = V + 1
adjlist = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int,input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)
visited = [0]*N     # visited 생성
stack = [0]*N       # stack 생성

dfs(1,N)
print()
