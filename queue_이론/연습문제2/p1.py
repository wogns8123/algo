def bfs(v,n):       # v : 시작점, n = 정점 개수
    visited = [0] *(n+1)
    q = []
    q.append(v)     # 시작점을 q에 저장
    visited[v] = 1  # 출발점 방문처리
    while q:
        v = q.pop(0)
        print(v)
        for w in lst[v]:
            if visited[w] == 0: # w가 방문한적 없으면!
                visited[w] += 1 # 방문처리

                q.append(w)     # q에 저장
    return

point,line = map(int,input().split())   # 점, 라인 개수
arr = list(map(int,input().split()))
lst = [[] for _ in range(point+1)]
for i in range(line):
    a, b = arr[i*2],arr[i*2+1]
    # a 는 출발점, b는 갈 수 있는 point번호
    lst[a].append(b)
    lst[b].append(a)

bfs(1,point)