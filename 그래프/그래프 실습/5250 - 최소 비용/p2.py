import heapq
import sys
sys.stdin=open('input.txt')
# 다익스트라:
#   가장 누적 거리가 짧은 것을 반복해서 가면, 최소비용을 알 수 있다.
#   가장 누적 거리가 짧은 것을 우선순위큐로 구현한다.
# 우선순위큐:
#   가장 우선순위가 높은 것을 큐에서 먼저 뺀다.  # heapq = 최소힙

def pdq():  # Priority Queue
    visited = [[1000000 for _ in range(N)] for _ in range(N)]  # U
    visited[0][0] = 0
    hq = []  # heapq
    heapq.heappush(hq, (0, 0, 0))  # 시작점
    while hq:
        pre_dis, x, y = heapq.heappop(hq)  # 현재누적거리, x, y
        if x == N-1 and y == N-1:          # 마지막 노드에 도착했으면
            break
        for gx, gy in ((x, y+1), (x+1, y), (x, y-1), (x-1, y)):  # 델타탐색
            if 0 <= gx < N and 0 <= gy < N:  # 그리드 안
                # 거리구하기
                if arr[gy][gx] > arr[y][x]:
                    dis = visited[y][x] + arr[gy][gx] - arr[y][x] + 1
                else:
                    dis = visited[y][x] + 1

                # 거리가 더 가까우면, 덮어씌우기, 교재에서 D의 효과
                if dis < visited[gy][gx]:
                    visited[gy][gx] = dis  # 짧은거리를 덮어씌운다.
                    heapq.heappush(hq, (dis, gx, gy))
    return visited[N-1][N-1]



TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list()
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    print(f'#{tc} {pdq()}')