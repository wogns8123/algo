import sys
sys.stdin = open('input.txt')

def bfs(start_i,start_j,arr):
    visited = [[0] * 17 for _ in range(17)]
    visited[start_i][start_j] = 1
    q = []
    q.append((start_i,start_j))
    while q:
        i,j = q.pop(0)
        if arr[i][j] == '2':
            return 1
        for di,dj in [[-1,0],[0,-1],[1,0],[0,1]]:
            ri, rj = i+di,j+dj
            if 0<=ri<len(arr) and 0<=rj<len(arr) and visited[ri][rj] == 0 and arr[ri][rj] != '1' :
                q.append((ri,rj))
                visited[ri][rj] = 1
    return 0
for test in range(10):
    num = int(input())
    arr = [list(input()) for _ in range(16)]

    # 시작점 찾기
    start_i, start_j = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == '3':
                start_i,start_j = i, j

    print(f'#{test+1} {bfs(start_i,start_j,arr)}')