# 2중 리스트
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)
#
# #
# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=' ')
#     print()

# 행,열 값 주는 2중 배열
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()

for i in range(N):
    for j in range(M):
        print(arr[i][j+(M-1-2*j) * (i%2)])