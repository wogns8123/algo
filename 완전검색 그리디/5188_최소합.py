import sys
sys.stdin = open('input.txt')

def bfs(start_i,start_j):
    visited = [[0]*n for _ in range(n)]
    queue = []
    queue.append((start_i,start_j))
    visited[start_i][start_j] = arr[0][0]
    while queue:
        x, y = queue.pop(0)
        for di, dj in [[0,1],[1,0]]:
            ri, rj = x+di, y+dj
            if ri>=n or rj >=n:
                pass
            else:
                next = arr[ri][rj] + visited[x][y]
                if visited[ri][rj] == 0:
                    visited[ri][rj] = next
                    queue.append((ri, rj))
                else:
                    if visited[ri][rj] > next:
                        visited[ri][rj] = next

    return visited[n-1][n-1]
tc = int(input())
for test in range(tc):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    print(f'#{test+1} {bfs(0,0)}')

