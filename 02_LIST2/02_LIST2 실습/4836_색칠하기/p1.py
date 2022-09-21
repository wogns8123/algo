import sys
sys.stdin = open("sample_input.txt")

tc = int(input())

for test in range(tc):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    count = 0
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if color == 1:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    elif arr[i][j] == 2:
                        arr[i][j] = 3
                        count += 1
                else:
                    if arr[i][j] == 0:
                        arr[i][j] = 2
                    elif arr[i][j] == 1:
                        arr[i][j] = 3
                        count += 1
    print(f'#{test+1} {count}')