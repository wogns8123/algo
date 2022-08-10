tc = int(input())

for test in range(tc):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    s = 0
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    s += abs(arr[i][j] - arr[ni][nj])
    print(f'#{test+1} {s}')
