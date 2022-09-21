import sys

sys.stdin = open('input.txt')

def bfs(start_i, start_j, arr):
    global count
    que = []
    que.append((start_i, start_j))
    count = 0
    while que:
        q = que.pop(0)
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ri, rj = q[0] + di, q[1] + dj
            if 0 <= ri < n and 0 <= rj < n and arr[ri][rj] == arr[q[0]][q[1]] + 1:
                que.append((ri, rj))

                count += 1
    return count

tc = int(input())
for test in range(tc):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    count_list = []
    count = 0
    ans1 = 0
    ans2 = 0
    result = []
    for i in range(n):
        for j in range(n):
            qwe = bfs(i, j, arr)
            if qwe > ans1:
                ans1 = qwe
                ans2 = arr[i][j]
            elif qwe == ans1:
                if ans2 > arr[i][j]:
                    ans2 = arr[i][j]

    print(f'#{test + 1} {ans2} {ans1}')