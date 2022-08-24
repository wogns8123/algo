def dfs(i,j,s,n):
    global minV
    if maze[i][j] == 3:
        if minV > s+1:  # 최단거리
            minV = s+1
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0,1],[1,0][0,-1],[0,-1]]:
            ni,nj = i+di,j+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                dfs(ni,nj,s+1,n)
        visited[i][j] = 0
        return
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
    answer = 0      # 경로의 수
    minV = n*n
    visited = [[0]*n for _ in range(n)]
    if minV == n*n:
        minv=-1
    dfs(sti,stj,0,n)