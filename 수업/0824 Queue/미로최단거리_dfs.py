def dfs(i,j,n):
    if maze[i][j] == 3:
        return
    else:
        visited[i][j] = 1
        for di, dj in [[0,1],[1,0][0,-1],[0,-1]]:
            ni,nj = i+di,j+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                dfs(ni,nj,n)
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
    visited = [[0]*n for _ in range(n)]

    dfs(sti,stj,n)