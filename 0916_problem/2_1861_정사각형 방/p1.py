import sys

sys.stdin = open('input.txt')
from collections import deque
def bfs(count):
    while que:
        q = que.popleft()
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ri, rj = q[0] + di, q[1] + dj
            if 0 <= ri < n and 0 <= rj < n  and arr[ri][rj] == arr[q[0]][q[1]] + 1:
                que.append((ri,rj))
        count += 1
    return count

tc = int(input())
for test in range(tc):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    count_list = []
    que = deque()
    result = []
    for i in range(n):
        for j in range(n):
            que.append((i, j))
            count = bfs(0)
            if count_list:
                if count > max(count_list):
                    result = []
                    count_list.append(count)
                    result.append(arr[i][j])
                elif count == max(count_list):
                    count_list.append(count)
                    result.append(arr[i][j])
            else:
                count_list.append(count)
                result.append(arr[i][j])


    print(f'#{test+1} {min(result)} {max(count_list)}')