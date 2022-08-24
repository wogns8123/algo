def bfs(i,j,n):
    visited = [[0]*n for _ in range(n)]
    q = []
    q.append((i,j))
    visited[i][j] = 1
    while q:
        i,j = q.pop(0)
        if maze[i][j] ==3:
            return 1
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] +1
    return 0
tc = int(input())
for test in range(tc):
    n = int(input())
    maze = [list(map(int,input())) for _ in range(n)]
    sti = -1
    stj = -1

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                sti,stj = i,j
                break
        if sti != -1:
            break


    print(f'#{test+1} {bfs(sti,stj,n)}')