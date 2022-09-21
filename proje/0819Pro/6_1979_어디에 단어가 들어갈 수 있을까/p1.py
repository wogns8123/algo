import sys
sys.stdin = open('input.txt')

tc = int(input())
for test in range(tc):

    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(M)]
    total = []

    for _ in range(2):
        for i in range(M):
            x = 0
            for j in range(M):
                if arr[i][j] == 1:
                    x += 1
                else:
                    total.append(x)
                    x = 0
            total.append(x)
        arr = [list(i) for i in zip(*arr)]
    result = total.count(N)
    print(f'#{test+1} {result}')