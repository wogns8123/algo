import sys

sys.stdin = open('sample_input.txt')


def move(arr):
    for i in range(N):
        for j in range(N):

            if arr[i][j] != [0]:
                if arr[i][j][1] == 1:
                    # arr[i - 1][j] = arr[i][j]
                    # list(arr[i - 1][j])
                    arr[i - 1][j].append(arr[i][j])
                    arr[i][j] = 0

                    # if i - 1 == 0 or i - 1 == N - 1 or j == 0 or j == N - 1:
                    #     arr[i - 1][j][1] += 1
                    #     arr[i - 1][j][0] //= 2

                elif arr[i][j][1] == 2:
                    # arr[i+1][j] = arr[i][j]
                    # list(arr[i + 1][j])
                    arr[i + 1][j].append(arr[i][j])
                    arr[i][j] = 0
                    # if i + 1 == 0 or i + 1 == N - 1 or j == 0 or j == N - 1:
                    #     arr[i + 1][j][1] -= 1
                    #     arr[i + 1][j][0] //= 2

                elif arr[i][j][1] == 3:
                    # arr[i][j-1] = arr[i][j]
                    # list(arr[i][j - 1])
                    arr[i][j - 1].append(arr[i][j])
                    arr[i][j] = 0
                    # if i == 0 or i == N - 1 or j - 1 == 0 or j - 1 == N - 1:
                    #     arr[i][j - 1][1] += 1
                    #     arr[i][j - 1][0] //= 2

                elif arr[i][j][1] == 4:
                    # arr[i][j+1] = arr[i][j]
                    # list(arr[i][j + 1])
                    arr[i][j + 1].append(arr[i][j])
                    arr[i][j] = 0
                    # if i == 0 or i == N - 1 or j + 1 == 0 or j + 1 == N - 1:
                    #     arr[i][j + 1][1] -= 1
                    #     arr[i][j + 1][0] //= 2


tc = int(input())
for test in range(tc):
    N, M, K = map(int, input().split())


    arr = [[[0] for _ in range(N)] for __ in range(N)]
    # arr = [[0]*N for _ in range(N)]
    for _ in range(K):
        i, j, micro, direction = map(int, input().split())
        arr[i][j] = [micro, direction]

    # for i in range(M):
    move(arr)
    # print(arr[1][1])
    for i in arr:
        # for j in i:
        #     print(j)
    #     for j in i:
    #         print(j)
        print(i)


