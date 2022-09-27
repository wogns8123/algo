import sys
sys.stdin = open('input.txt')

def backtracking(row,n,total,visited):
    global min_idx
    if row == n:    # 끝까지 갔으면
        if total <= min_idx:
            min_idx = total
    elif total > min_idx:   # total이 min보다 크면 중지
        return
    else:
        for q in range(n):      # visited 방문하면서
            if visited[q] == 0:
                visited[q] = 1
                backtracking(row+1,n,total+arr[row][q],visited)
                visited[q] = 0

tc = int(input())
for test in range(tc):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_idx = 1111111111111111
    visited = [0] *N

    backtracking(0,N,0,visited)
    print(f'#{test+1} {min_idx}')
