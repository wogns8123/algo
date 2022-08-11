import sys
sys.stdin = open('input.txt')

tc = int(input())
for i in range(tc):
    arr = [list(map(int,input().split())) for _ in range(100)]
    start = []
    di = [-1, 0, 0]
    dj = [0, 1, -1]
    i,j = 0, 99
    # 도착지의 위치를 찾기 위해
    for i in range(100):
        for j in range(100):
            if arr[i][j] ==2:
                start = [i, j]
    #
    while True :
        if

    for i in range(1, 100-1):
        for j in range(1, 100-1):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 < ni <100 and 0 <= nj <100:
                    if






