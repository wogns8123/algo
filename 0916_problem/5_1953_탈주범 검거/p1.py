import sys

sys.stdin = open('input.txt')


def change(N, M, arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                if 0 <= i - 1 < N and (arr[i - 1][j] in [1, 2, 5, 6]) or (0 <= j + 1 < M and (arr[i][j + 1] in [1, 3, 6, 7])) or (0 <= i + 1 < N and (arr[i + 1][j] in [1, 2, 4, 7])) or (0 <= j - 1 < M and (arr[i][j - 1] in [1, 3, 4, 5])):  # 상
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0

            elif arr[i][j] == 2:
                if 0 <= i - 1 < N and (arr[i - 1][j] in [1, 2, 5, 6]) or 0 <= i + 1 < N and (arr[i + 1][j] in [1, 2, 4, 7]):  # 상 하
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0

            elif arr[i][j] == 3:
                if 0 <= j + 1 < M and (arr[i][j + 1] in [1, 3, 6, 7]) or (0 <= j - 1 < M and (arr[i][j - 1] in [1, 3, 4, 5])):  # 우 좌
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0

            elif arr[i][j] == 4:
                if i - 1 >= 0 and (arr[i - 1][j] in [1, 2, 5, 6]) or (0 <= j + 1 < M and (arr[i][j + 1] in [1, 3, 6, 7])):  # 상 우
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0

            elif arr[i][j] == 5:
                if 0 <= j + 1 < M and (arr[i][j + 1] in [1, 3, 6, 7]) or (0 <= i + 1 < N and (arr[i + 1][j] in [1, 2, 4, 7])):  # 우 하
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0

            elif arr[i][j] == 6:
                if 0 <= i + 1 < N and (arr[i + 1][j] in [1, 2, 4, 7]) or (0 <= j - 1 < M and (arr[i][j - 1] in [1, 3, 4, 5])):  # 하 좌
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0

            elif arr[i][j] == 7:
                if i - 1 >= 0 and (arr[i - 1][j] in [1, 2, 5, 6]) or (0 <= j - 1 < M and (arr[i][j - 1] in [1, 3, 4, 5])):  # 상 좌
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0
    return arr

def bfs(start_i, start_j, visited,time):  # start_i = R , j = C
    que = []
    visited[start_i][start_j] = 1
    que.append((start_i,start_j))

    while que:
        q = que.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ri = q[0] + di
            rj = q[1] + dj
            if 0<=ri<N and 0<=rj<M and visited[ri][rj] == 0 and arr[ri][rj] == 1:
                visited[ri][rj] += 1+visited[q[0]][q[1]]
                que.append((ri,rj))
        if visited[ri][rj] == time:
            break


tc = int(input())
for test in range(tc):
    N, M, R, C, time = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    count = 0
    change(N, M, arr)
    bfs(R,C,visited,time)
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                count +=1

    print(count)