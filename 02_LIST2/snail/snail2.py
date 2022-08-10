tc= int(input())
for test in range(tc):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    a, b = 0, 0
    count = 1
    d = 0               # 방향 조절용

    for i in range(n):
        for j in range(n):
            arr[a][b] = count
            a = a + di[d]
            b = b + dj[d]
            if not 0 <= a <= n or 0 <= b <= n or arr[i][j] != 0:
                a -= di[d]
                b -= dj[d]

                d = (d + 1) % 4
                a += di[d]
                b += dj[d]
            count += 1
        print(arr)
