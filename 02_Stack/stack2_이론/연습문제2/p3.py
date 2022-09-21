def f(i, N):
    if i == N:
        s = 0
        for i in range(N):  # 부분집합의 합 : s
            if bit[i] == 1:
                s += arr[i]
        if s == 10:             # 합이 10일 경우 출력
            for i in range(N):
                if bit[i] == 1:
                    print(arr[i], end=' ')
            print()
    else:                  # bit[i]가 1인 경우와 0인 경우 나뉘어짐
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * len(arr)
f(0, 10)
