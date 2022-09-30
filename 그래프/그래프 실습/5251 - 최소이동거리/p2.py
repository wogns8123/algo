import sys
sys.stdin = open('input.txt')

def bfs(n):
    q = [n]
    while q:
        node= q.pop(0)
        for i in range(N+1):
            if arr[node][i] > 0 and distance[i] > distance[node] + arr[node][i]:
                distance[i] = distance[node] + arr[node][i]
                q.append(i)


tc = int(input())
for test in range(tc):
    N,E = map(int,input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    distance = [0] + [9999] * N

    for _ in range(E):
        start, end, w = map(int,input().split())
        arr[start][end] = w
    bfs(0)
    print(f'#{test+1} {distance[-1]}')
