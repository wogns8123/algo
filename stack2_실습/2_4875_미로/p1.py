import sys
sys.stdin=open('sample_input.txt')

tc = int(input())
for test in range(tc):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    ni = [0, 0, 1, -1]
    nj = [1, -1, 0, 0]  # 상하우좌
    start_i,start_j = 0, 0  # 출발점 위치
    result = 0          # 도착 여부 확인용

    # 출발점 위치 확인
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                start_i,start_j = i, j
    stack = [(start_i,start_j)]
    visited = [(start_i,start_j)]       # 방문한 곳 저장하는 stack

    while stack:
        i,j = stack.pop()               # 0인 공간으로 이동하면 시작점도 바뀌어야함
        for k in range(4):
            ri = i + ni[k]
            rj = j + nj[k]
            if 0 <= ri < n and 0 <= rj < n:
                if arr[ri][rj] == '3':  # 도착지를 찾으면 result에 1을 저장 후 break
                    result = 1
                    break
                elif arr[ri][rj] == '0' and (ri,rj) not in visited: # 0이고 간 적이 없는 곳이면 visited와 stack에 저장
                    visited.append((ri,rj))
                    stack.append((ri,rj))

    print(f'#{test+1} {result}')