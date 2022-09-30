import heapq
def f():
    visited = [[100000 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    heap = []
    heapq.heappush(heap,(0,0,0))

    while heap:
        distance, x, y = heapq.heappop(heap)
        if x == N-1 and y == N-1:
            break
        for rx,ry in ((x,y+1),(x+1,y),(x,y-1),(x-1,y)):
            if 0<=rx<N and 0<=ry<N:
                if arr[ry][rx] > arr[y][x]:
                    distance = visited[y][x] + arr[ry][rx] - arr[y][x] + 1
                else:
                    distance = visited[y][x] + 1
                if distance < visited[ry][rx]:
                    visited[ry][rx] = distance
                    heapq.heappush(heap,(distance,rx,ry))
    return visited[N-1][N-1]



tc = int(input())
for test in range(tc):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    print(f'#{test+1} {f()}')