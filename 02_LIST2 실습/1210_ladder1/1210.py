import sys
sys.stdin = open('input.txt')


for test in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    start = []
    di = [-1, 0, 0]
    dj = [0, 1, -1]

    idx = 0
    # 도착지의 위치를 찾기 위해
    for i in range(100):
        for j in range(100):
            if arr[i][j] ==2:
                break

    # start 위치에서 꼭대기로 이동(가는 길에 di, dj를 이용해 델타 탐색)
    while i>0:
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0<=ni<100 and 0<=nj<100:
            if arr[ni][nj] ==1:
                i = ni
                j = nj
                arr[ni][nj] = -1
        idx = (idx+1)%3
    print(f'#{test+1} {j}')





