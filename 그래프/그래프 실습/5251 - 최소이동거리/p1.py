import sys
sys.stdin=open('input.txt')

def bfs(n):
    q = [n]
    while q:
        v = q.pop(0)
        for i in range(N + 1):
            if adjM[v][i] > 0 and distance[i] > distance[v] + adjM[v][i]:   # 가중치가 존재하고, 이동할 노드쪽의 거리가 내가 곧 이동할 거리의 합보다 작으면 이동
                distance[i] = distance[v] + adjM[v][i]                      # 누적 거리 갱신
                q.append(i)

T = int(input())
for test in range(1, T + 1):
    N, E = map(int, input().split())
    adjM = [[0] * (N + 1) for _ in range(N + 1)]            # 가중치를 입력받을 인접행렬
    distance = [0] + [float('inf')] * (N)                   # 거리값을 받을 변수

    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w
    bfs(0)
    print(f'#{test} {distance[-1]}')

