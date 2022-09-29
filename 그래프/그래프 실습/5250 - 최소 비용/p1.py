import sys
sys.stdin=open('input.txt')

# def DFS(start_i,start_j):
#     stack = [(start_i,start_j)]
#     visited = [[0]*(N) for _ in range(N)]
#     while stack:
#         node = stack.pop()
#         for di,dj in [[1,0],[0,1]]:
#             ri,rj= node[0]+di, node[1]+dj
#             if 0<=ri<N and 0<=rj<N and
#     print(visited)


tc = int(input())
for test in range(tc):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dp = [[0]*N for _ in range(N)]

    for j in range(N):
        dp[0][j] = dp[0][j] + abs(arr[0][j-1]-arr[0][j])
    print(dp)