for test in range(10):
    test_number = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    N = len(arr)
    x_sum = []
    y_sum = []
    right_sum = 0  # 오른쪽 아래로 향하는 대각선
    left_sum = 0   # 왼쪽 아래로 향하는 대각선
    # 대각선의 합
    for i in range(N):
        right_sum += arr[i][i]
        left_sum += arr[i][N-i-1]

    # 가로의 합
    for i in range(N):
        total = 0
        for j in range(N):
            total += arr[i][j]
        x_sum.append(total)
    # 세로의 합
    for i in range(N):
        total = 0
        for j in range(N):
            total += arr[j][i]
        y_sum.append(total)
    # 가로 중 가장 큰 값
    max_x = 0
    for i in range(len(x_sum)):
        if max_x < x_sum[i]:
            max_x = x_sum[i]

    # 세로 중 가장 큰 값
    max_y = 0
    for i in range(len(y_sum)):
        if max_x < y_sum[i]:
            max_x = y_sum[i]
    # 이제 max_x, max_y, right_sum, left_sum값 비교
    a = [max_x, max_y, right_sum, left_sum]

    result = 0
    for i in range(len(a)):
        if result < a[i]:
            result = a[i]
    print(f'#{test+1} {result}')