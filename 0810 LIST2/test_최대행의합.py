N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

max_V = 0               # 최대 행의 합
for i in range(N):
    s = 0
    for j in range(N):  # i행의 j열에 접근
        s += arr[i][j]
    if max_V < s:
        max_V = s
print(max_V)

