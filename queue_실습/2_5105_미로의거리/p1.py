import sys
sys.stdin = open('sample_input.txt')

def bfs(arr,start_i, start_j, num):
    visited = [[0]*num for _ in range(num)]  # 간 곳
    visited[start_i][start_j] = 1  # 방문 처리
    queue = []
    queue.append((start_i,start_j))
    while queue:
        i,j = queue.pop(0)
        if arr[i][j] == '3':            # 3을 만나면 return
            return visited[i][j]-2      # 시작이 1부터 시작하고 목적지가 3의 전까지 계산하기때문에 2을 뺌
        else:
            for di, dj in [[-1, 0], [0, 1], [0, -1], [1, 0]]:   #상 우 좌 하
                ri = di + i
                rj = dj + j
                if 0<=ri<num and 0<=rj<num and arr[ri][rj] != '1' and visited[ri][rj] == 0:
                    queue.append((ri,rj))
                    visited[ri][rj] = visited[i][j]+1
    return 0

tc = int(input())
for test in range(tc):
    num = int(input())
    arr = [list(input()) for _ in range(num)]

    # 시작점 찾기
    start_i = 0
    start_j = 0
    for i in range(num):
        for j in range(num):
            if arr[i][j] == '2':
                start_i, start_j = i, j

    print(f'#{test+1} {bfs(arr,start_i,start_j, num)}')

